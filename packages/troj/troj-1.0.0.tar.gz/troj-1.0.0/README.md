# TrojAI Integration Package
TrojAI provides the troj Python convenience package to allow users to integrate TrojAI adversarial protections and robustness metrics seamlessly into their AI development pipelines.

## Installation
Run the following to install:
```python
pip install troj["dev"]
pip install troj["nlp"]
pip install troj["cv"]
```

## Usage
The troj package has support for Image Classification and Object Detection tasks. The notebooks in the demos folder contain examples to get set up on either task using PyTorch or TensorFlow (limited support for now). The test_troj.py file also contains our tests that run on deployment and could also be helpful for understanding our API better.

One more thing is that our package expects specific data formats for now until we can support more formats.
The two formats are described by the following:
```python
'''
ImageNet folder style (Image Classification): 
/train
----/class1
----/class2
...
/test
----/class1
----/class2
...etc 

CoCo annotation style (Object Detection):
/images
----image1.jpg
----image2.jpg
...etc
annotation.json

'''

```

## Examples
Example notebooks for many use cases are contained in the demos folder. If there are errors in the notebook, cross reference the syntax with test_troj.py, the tests will always contain the most updated working version of our packages and the notebooks may lag a bit. 

## Command Line Tool
Troj package use via command line is currently in development. After package install the command line tool can be accessed through the command "troj" which currently takes two arguments, an attacking config file and a user config file to authenticate with our AWS infrastructure. The command line files can be found under trojai/cmd. If you want to run the NLP demo we currently have setup, try out the following command:

```
 troj --c "trojai\cmd\example.json" --a "trojai\cmd\user-config.json"
```
   
## How to develop locally (MOSTLY INTERNAL ONLY)
Here are three commands to run after cloning the repo to install the cloned version to your environment (changes in code will be reflected immediately if using this).
```
pip install wheel
python setup.py bdist_wheel
pip install -e.[dev]
```

## How to build and upload to pypi (INTERNAL ONLY)
Build the package under dist folder using this, will create tar.gz and .whl for version id in setup.py:
```
python -m build
```

Upload it to testpypi repo using this (remove --repository flag to go live, make sure dist only has the files you expect):
```
Dev Package:
    python -m twine upload --repository testpypi dist/*
prod package:
    python -m twine upload dist/*
```

When install from testpypi repo you need this format: pip install --extra-index-url https://test.pypi.org/simple/ package_name_here https://stackoverflow.com/questions/51589673/pip-install-producing-could-not-find-a-version-that-satisfies-the-requirement - otherwise dependency packages wont be looked for on live pypi
