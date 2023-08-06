import numpy as np
from PIL import Image
import os
from torchvision import transforms
import random
from .Corruptions import *
import json
import copy

'''
This code is a slightly modified version of https://github.com/bethgelab/imagecorruptions.
'''

corruption_tuple = (gaussian_noise, shot_noise, impulse_noise, defocus_blur,
                    glass_blur, motion_blur, zoom_blur, snow, frost, fog,
                    brightness, contrast, elastic_transform, pixelate,
                    jpeg_compression, speckle_noise, gaussian_blur, spatter,
                    saturate)

corruption_dict = {corr_func.__name__: corr_func for corr_func in
                   corruption_tuple}

#TODO ensure OD dataset making tools can be used generically.

def corrupt(image, severity=1, corruption_name=None, corruption_number=-1):
    '''

    :param image: image to corrupt; a numpy array in [0, 255], expected datatype is np.uint8
                                    expected shape is either (height x width x channels) or (height x width);
                                    width and height must be at least 32 pixels;
                                    channels must be 1 or 3;
    :param severity: strength with which to corrupt the image; an integer in [1, 5]
    :param corruption_name: specifies which corruption function to call, must be one of
                                        'gaussian_noise', 'shot_noise', 'impulse_noise', 'defocus_blur',
                                        'glass_blur', 'motion_blur', 'zoom_blur', 'snow', 'frost', 'fog',
                                        'brightness', 'contrast', 'elastic_transform', 'pixelate', 'jpeg_compression',
                                        'speckle_noise', 'gaussian_blur', 'spatter', 'saturate';
    :param corruption_number: the position of the corruption_name in the above list; an integer in [0, 18];
                                        useful for easy looping; 15, 16, 17, 18 are validation corruption numbers
    :return: Numpy array for the corrupted image.
    '''

    if not isinstance(image, np.ndarray):
        raise AttributeError('Expecting type(image) to be numpy.ndarray')
    if not (image.dtype.type is np.uint8):
        raise AttributeError('Expecting image.dtype.type to be numpy.uint8')

    if not (image.ndim in [2, 3]):
        raise AttributeError('Expecting image.shape to be either (height x width) or (height x width x channels)')
    if image.ndim == 2:
        image = np.stack((image,) * 3, axis=-1)

    height, width, channels = image.shape

    if (height < 32 or width < 32):
        raise AttributeError('Image width and height must be at least 32 pixels')

    if not (channels in [1, 3]):
        raise AttributeError('Expecting image to have either 1 or 3 channels (last dimension)')

    if channels == 1:
        image = np.stack((np.squeeze(image),) * 3, axis=-1)

    if not severity in [1, 2, 3, 4, 5]:
        raise AttributeError('Severity must be an integer in [1, 5]')

    if not (corruption_name is None):
        image_corrupted = corruption_dict[corruption_name](Image.fromarray(image),
                                                           severity)
    elif corruption_number != -1:
        image_corrupted = corruption_tuple[corruption_number](Image.fromarray(image),
                                                              severity)
    else:
        raise ValueError("Either corruption_name or corruption_number must be passed")

    return np.uint8(image_corrupted)



def TorchCorrupt(image,  severity=1, corruption_name=None, corruption_number=-1):
    '''
    Applies corruptions to Pytorch tensors.

    :param image: image to corrupt; a Pytorch tensor with values between [0,1] with width and height at least 32 by 32,
    with 1 or 3 channels.
    :param severity: strength with which to corrupt the image; an integer in [1, 5]
    :param corruption_name: specifies which corruption function to call, must be one of
                                        'gaussian_noise', 'shot_noise', 'impulse_noise', 'defocus_blur',
                                        'glass_blur', 'motion_blur', 'zoom_blur', 'snow', 'frost', 'fog',
                                        'brightness', 'contrast', 'elastic_transform', 'pixelate', 'jpeg_compression',
                                        'speckle_noise', 'gaussian_blur', 'spatter', 'saturate';
    :param corruption_number: the position of the corruption_name in the above list; an integer in [0, 18];
                                        useful for easy looping; 15, 16, 17, 18 are validation corruption numbers
    :return: Torch tensor for the corrupted image.
    '''
    if type(image)==np.ndarray:
        im_shape = image.shape
        if image.shape[0]==3:
            image = image.reshape(im_shape[1], im_shape[2], im_shape[0])
        if image.dtype != 'uint8':
            image=image*255
            image = np.uint8(image)
        corrupted = corrupt(image, severity, corruption_name, corruption_number)
        image = corrupted.reshape(im_shape[0], im_shape[1], im_shape[2])
        image = np.float32(image/255)

    else:
        image = transforms.ToPILImage()(image.detach().cpu())
        image = np.asarray(image)
        corrupted = corrupt(image, severity, corruption_name, corruption_number)
        image = Image.fromarray(np.uint8(corrupted))
        image = transforms.ToTensor()(image)
    return image

def corruption_class_builder(corruption_name):
    '''
    A tool for making corruptions available as a transfromation attack under the CLI. Takes in a corruption name
    and returns a transformation compatible class for the desired corruption

    :param corruption_name:
    :return:
    '''
    class CorruptionTransformation:
        def __init__(self, severity):
            self.corruption = corruption_name
            self.severity = severity

        def __call__(self, image):
            return TorchCorrupt(image, self.severity, self.corruption)
    return CorruptionTransformation


def get_corruption_names(subset='common'):
    '''
    Retrieves corruption names.

    :param subset: An optional subset to retrieves, must be one of
    ``['common', 'validation', 'all', 'noise', 'blur', 'weather',  'digital']``
    :return: A list of corruption names.
    '''
    if subset == 'common':
        return [f.__name__ for f in corruption_tuple[:15]]
    elif subset == 'validation':
        return [f.__name__ for f in corruption_tuple[15:]]
    elif subset == 'all':
        return [f.__name__ for f in corruption_tuple]
    elif subset == 'noise':
        return [f.__name__ for f in corruption_tuple[0:3]]
    elif subset == 'blur':
        return [f.__name__ for f in corruption_tuple[3:7]]
    elif subset == 'weather':
        return [f.__name__ for f in corruption_tuple[7:11]]
    elif subset == 'digital':
        return [f.__name__ for f in corruption_tuple[11:15]]
    else:
        raise ValueError("subset must be one of ['common', 'validation', 'all']")


def FormatCorruptDataframe(df):
    '''
    Takes in a dataframe with a column called `file_name` where the files follow the corruption naming convention of
    `original_file_name + '_cor_{}_sev_{}'.format(corruption, severity) + extension`, and returns a dataframe with two
    new columns, one for the severity and one for the corruption type.

    :param df: A troj dataframe built from a corrupted dataset.
    :returns: Returns the original dataframe with two new columns, one for corruption type and the other for severity.
    '''
    corruption_names = []
    severities = []
    file_names = df['file_name'].tolist()
    for f_name in file_names:
        retrieve_split = f_name.split('_cor_')
        second_split = retrieve_split[-1].split('_sev_')
        corruption_names.append(second_split[0])
        severities.append(second_split[-1].split('.')[0])
    df['severity'] = severities
    df['corruption_type'] = corruption_names
    return df


def im_loc_splitter_classification(location):
    '''
    Retrieves the class of the image and the filename for classification datasets.

    :param location: Location of image file.
    :returns: The class of the image and the filename
    '''
    folderwise_split = location.split('/')
    img_file = folderwise_split[-1]
    img_class = folderwise_split[-2]
    return img_file, img_class




def rename_img(img_file, corruption_name, severity):
    '''
    :param img_file: name of the image file
    :param corruption_name: corruption name
    :param severity: severity of the corruption
    :returns: new file name for corrupt image in format {original name}_cor_{corruption name}_sev_{severity of corruption}.extension
    '''
    split_file_extension = img_file.split('.')
    file_extension = '.{}'.format(split_file_extension[-1])
    img_name_extension = '_cor_{}_sev_{}'.format(corruption_name, severity)
    corrupt_img_name = split_file_extension[0] + img_name_extension + file_extension
    return corrupt_img_name




def corrupt_and_save_classification(original_location, new_root, corruption, severity, image_array=None):
    '''
    :param original_location: Original image location.
    :param new_root: The new root folder.
    :param corruption: The corruption to apply.
    :param severity: The severity of the corruption.
    :param image_array: A preloaded image array, if none, the image is loaded from the original_location parameter
    :returns: saves corrupt image at the location {new_root}/{class}/{corrupt image name}

    '''
    im_file, im_class = im_loc_splitter_classification(original_location)
    corrupt_im_name = rename_img(im_file, corruption, severity)
    save_loc = os.path.join(new_root, im_class)
    if os.path.exists(new_root)==False:
        os.makedirs(new_root)
    if os.path.exists(os.path.join(new_root, im_class))==False:
        os.makedirs(save_loc)
    if image_array is None:
        image_array=np.asarray(Image.open(original_location))
    original_image = image_array
    corrupted = corrupt(original_image, corruption_name=corruption, severity=severity)
    corrupted_image = Image.fromarray(corrupted)
    corrupted_image.save(os.path.join(save_loc, corrupt_im_name))


def corrupt_dset_random(original_folder, new_folder, corruptions, severities,  include_original=False, verbose=True):
    '''
    :param original_folder: The original split folder (test folder).
    :param new_folder: New folder location to save corrupt images to.
    :param corruptions: A list of corruptions.
    :param severities: A list of severity levels.
    :param include_original: Whether or not to include the original image in the new test set.
    :param verbose: Whether or not to print generation progress.
    :returns: Creates a new dataset at new_folder containing images which are corrupted according to a random sampling
    of the corruptions and severity
    '''
    classes = os.listdir(original_folder)
    num_classes = len(classes)
    class_counter = 0
    if os.path.exists(new_folder)==False:
        os.makedirs(new_folder)
    for class_name in classes:
        class_counter += 1
        im_counter = 0
        class_folder = os.path.join(original_folder, class_name)
        im_files = os.listdir(class_folder)
        num_imgs = len(im_files)
        new_class_folder = os.path.join(new_folder, class_name)
        if os.path.exists(new_class_folder) == False:
            os.makedirs(new_class_folder)
        for img_file in im_files:
            im_counter += 1
            im_loc = os.path.join(class_folder, img_file)
            image = Image.open(im_loc)
            if include_original==True:
                uncorrupt_name= rename_img(img_file, 'none', 0)
                image.save(os.path.join(new_class_folder, uncorrupt_name))
            image_arr = np.asarray(image)
            corrupt_name = random.choice(corruptions)
            severity = random.choice(severities)
            corrupt_and_save_classification(im_loc, new_folder, corrupt_name, severity, image_arr)
            if verbose==True:
                progress_str = 'Class {}/{}: Image {}/{}'.format(class_counter, num_classes, im_counter, num_imgs)
                print(progress_str)




def corrupt_dset_all(original_folder, new_folder, corruptions, severities,  include_original=False, verbose=True):
    '''
    :param original_folder: The original split folder (test folder).
    :param new_folder: New folder location to save corrupt images to.
    :param corruptions: A list of corruptions.
    :param severities: A list of severity levels.
    :param include_original: Whether or not to include the original image in the new test set.
    :param verbose: Whether or not to print generation progress.
    :returns: Creates a new dataset at new_folder where every image is corrupted by each corruption and each severity and saved.
    '''
    classes = os.listdir(original_folder)
    num_classes = len(classes)
    class_counter = 0
    if os.path.exists(new_folder)==False:
        os.makedirs(new_folder)
    for class_name in classes:
        class_counter += 1
        im_counter = 0
        class_folder = os.path.join(original_folder, class_name)
        im_files = os.listdir(class_folder)
        num_imgs = len(im_files)
        new_class_folder = os.path.join(new_folder, class_name)
        if os.path.exists(new_class_folder) == False:
            os.makedirs(new_class_folder)
        for img_file in im_files:
            im_counter += 1
            im_loc = os.path.join(class_folder, img_file)
            image = Image.open(im_loc)
            if include_original==True:
                uncorrupt_name= rename_img(img_file, 'none', 0)
                image.save(os.path.join(new_class_folder, uncorrupt_name))
            image_arr = np.asarray(image)
            for corrupt_name in corruptions:
                for severity in severities:
                    corrupt_and_save_classification(im_loc, new_folder, corrupt_name, severity, image_arr)
            if verbose==True:
                progress_str = 'Class {}/{}: Image {}/{}'.format(class_counter, num_classes, im_counter, num_imgs)
                print(progress_str)



def MakeCorruptDsetClassification(original_folder, new_folder, corruptions, severities, mode='random',  include_original=False, verbose=True):
    '''
    Makes a corrupted dataset for classification problems which is compatible with the ART integration.

    :param original_folder: The original split folder (test folder).
    :param new_folder: New folder location to save corrupt images to.
    :param corruptions: A list of corruptions.
    :param severities: A list of severity levels.
    :param mode: One of either 'random' or 'all'. If random, each image is corrupted by randomly sampling a corruption and severity level.
    If all, every corruption and every severity is applied to each image one at a time and saved.
    :param include_original: Whether or not to include the original image in the new test set.
    :param verbose: Whether or not to print generation progress.
    :returns: Creates a new dataset at new_folder containing corrupt images.
    '''
    if mode.lower()=='random':
        corrupt_dset_random(original_folder, new_folder, corruptions, severities, include_original, verbose)
    if mode.lower()=='all':
        corrupt_dset_all(original_folder, new_folder, corruptions, severities, include_original, verbose)



def change_annotation_imfile(annot_dict, corruption_name, severity):
    '''
    Changes the image file name in the annotation dictionary.
    :param annot_dict: Annotation dictionary for an image.
    :param corruption_name: Name of the corruption applied to the image.
    :param severity: How severe the corruption is.
    :return: The annotations with the new image name.
    '''
    annot_dict_copy = copy.deepcopy(annot_dict)
    img_file = annot_dict['file_name']
    corrupt_name = rename_img(img_file, corruption_name, severity)
    annot_dict_copy['file_name'] = corrupt_name
    return annot_dict_copy



def corrupt_and_save_OD(annot_dict, old_root, new_root, corruption, severity, image_array=None):
    '''
    :param annot_dict: Annotation dictionary for the example
    :param old_root: root folder for the old image
    :param new_root: The new root folder.
    :param corruption: The corruption to apply.
    :param severity: The severity of the corruption.
    :param image_array: A preloaded image array, if none, the image is loaded from the original_location parameter
    :returns: saves corrupt image at the location {new_root}/{corrupt image name}, and returns the new annotation dictionary
    '''
    original_location = os.path.join(old_root, annot_dict['file_name'])
    new_annotation_dict = change_annotation_imfile(annot_dict, corruption, severity)
    save_loc = os.path.join(new_root, new_annotation_dict['file_name'])
    if os.path.exists(new_root)==False:
        os.makedirs(new_root)
    if image_array is None:
        image_array=np.asarray(Image.open(original_location))
    original_image = image_array
    corrupted = corrupt(original_image, corruption_name=corruption, severity=severity)
    corrupted_image = Image.fromarray(corrupted)
    corrupted_image.save(save_loc)
    return new_annotation_dict




def corrupt_od_dset_random(original_folder, new_folder, annot_save_loc, annotations, corruptions, severities, include_original=False, verbose=True):
    '''
    :param original_folder: Original folder location.
    :param new_folder: Folder location for new images
    :param annot_save_loc: File path for new annotations, saved in Troj format.
    :param annotations: Annotations dictionary in Troj format.
    :param corruptions: List of corruptions.
    :param severities: List of severities
    :param include_original: Whether or not to include the original image in the new dataset.
    :param verbose: Whether or not to print the progress of the corruptions.
    '''
    corruptions_annot_dict = {}
    counter = 0
    if os.path.exists(new_folder)==False:
        os.makedirs(new_folder)
    for im_key in list(annotations.keys()):
        im_annots = annotations[im_key]
        corrupt_name = random.choice(corruptions)
        severity = random.choice(severities)

        original_im_loc = os.path.join(original_folder, im_annots['file_name'])
        image = Image.open(original_im_loc)
        if include_original:
            corruptions_annot_dict[str(im_key)] = im_annots
            image.save(os.path.join(new_folder, im_annots['file_name']))
        image_arr = np.asarray(image)
        new_annots = change_annotation_imfile(im_annots, corrupt_name, severity)
        new_key = str(im_key) + '_cor_{}_sev_{}'.format(corrupt_name, severity)
        corruptions_annot_dict[new_key] = new_annots
        corrupted = corrupt(image_arr, corruption_name=corrupt_name, severity=severity)
        corrupted_image = Image.fromarray(corrupted)
        corrupted_image.save(os.path.join(new_folder, new_annots['file_name']))
        if verbose:
            print('{}/{} Images corrupted and saved.'.format(counter, len(annotations)))
            counter += 1
    with open(annot_save_loc, 'w') as fp:
        json.dump(corruptions_annot_dict, fp)
    return corruptions_annot_dict




def corrupt_od_dset_all(original_folder, new_folder, annot_save_loc, annotations, corruptions, severities, include_original=False, verbose=True):
    '''
    :param original_folder: Original folder location.
    :param new_folder: Folder location for new images
    :param annot_save_loc: File path for new annotations, saved in Troj format.
    :param annotations: Annotations dictionary in Troj format.
    :param corruptions: List of corruptions.
    :param severities: List of severities
    :param include_original: Whether or not to include the original image in the new dataset.
    :param verbose: Whether or not to print the progress of the corruptions.
    '''
    corruptions_annot_dict = {}
    counter = 0
    if os.path.exists(new_folder)==False:
        os.makedirs(new_folder)
    for im_key in list(annotations.keys()):
        im_annots = annotations[im_key]

        original_im_loc = os.path.join(original_folder, im_annots['file_name'])
        image = Image.open(original_im_loc)
        if include_original:
            corruptions_annot_dict[str(im_key)] = im_annots
            image.save(os.path.join(new_folder, im_annots['file_name']))
        image_arr = np.asarray(image)
        for corrupt_name in corruptions:
            for severity in severities:
                new_annots = change_annotation_imfile(im_annots, corrupt_name, severity)
                new_key = str(im_key) + '_cor_{}_sev_{}'.format(corrupt_name, severity)
                corruptions_annot_dict[new_key] = new_annots
                corrupted = corrupt(image_arr, corruption_name=corrupt_name, severity=severity)
                corrupted_image = Image.fromarray(corrupted)
                corrupted_image.save(os.path.join(new_folder, new_annots['file_name']))
        if verbose:
            print('{}/{} Images corrupted and saved.'.format(counter, len(annotations)))
            counter += 1
    with open(annot_save_loc, 'w') as fp:
        json.dump(corruptions_annot_dict, fp)
    return corruptions_annot_dict




def MakeCorruptDsetOD(original_folder, new_folder, annot_save_loc, annotations, corruptions, severities, mode='random',  include_original=False, verbose=True):
    '''
    Makes a corrupted dataset from some task which contains the image location in the annotations. Originally used for simplyobject detection,
    but can easily be used for other tasks.

    :param original_folder: The original split folder (test folder).
    :param new_folder: New folder location to save corrupt images to.
    :param annot_save_loc: File path for new annotations, saved in Troj format.
    :param annotations: Annotations dictionary in Troj format.
    :param corruptions: A list of corruptions.
    :param severities: A list of severity levels.
    :param mode: One of either 'random' or 'all'. If random, each image is corrupted by randomly sampling a corruption and severity level.
    If all, every corruption and every severity is applied to each image one at a time and saved.
    :param include_original: Whether or not to include the original image in the new test set.
    :param verbose: Whether or not to print generation progress.
    :returns: Creates a new dataset at new_folder containing corrupt images.
    '''
    if mode.lower()=='random':
        corrupt_annotations = corrupt_od_dset_random(original_folder, new_folder, annot_save_loc, annotations, corruptions, severities, include_original, verbose)
    if mode.lower()=='all':
        corrupt_annotations = corrupt_od_dset_all(original_folder, new_folder, annot_save_loc, annotations, corruptions, severities, include_original, verbose)
    return corrupt_annotations
