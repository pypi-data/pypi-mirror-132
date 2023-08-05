# TunAugmentor
TunAugmentor is a python library for image data augmentation. Image augmentation is an effective technique widely used for Machine Learning and Computer Vision tasks.
The aim of image augmentation is to apply different transformations on existing images to create more data for the model hence increasing the performance of the model.
Therefore, it is the process of increasing the training dataset without collecting new data.
## Table of contents
- [About TunAugmentor](#About-TunAugmentor)
- [Authors](#Authors)
- [Installation](#Installation)
- [Example](Example)
- [Transformation List](#Transformation-List)
  - [CenterCrop](#CenterCrop)
  - [Crop](#Crop)
  - [CropAndPad](#CropAndPad)
  - [CropOrPad](#CropOrPad)
  - [Flip](#Flip)
  - [Flip Horizontal](#FlipHorizontal)
  - [FlipVertical](#FLipVertical)
  - [Identity](#Identity)
  - [Transpose](#Transpose)
  - [RandomCrop](#RandomCrop)
  - [RandomRotation90](#RandomRotation90)
## About TunAugmentor
- The aim of this project was to reimplement different image augmentation techniques using only Python and Numpy. We do not claim we reinvented the wheel. We know theese techniques are already available in different libraries with better implementations and you should probably use theese instead. The goal was to learn to implement this techniques and to try to distribute a Python Library. Thus, we didn't do any benchmarking for this work.
- [Albumentations](https://github.com/albumentations-team/albumentations) was a great source of inspiration concerning which transformation to implement and for the documentation. Try to check their work you may find what you really need.
## Authors
- [Ahmed Belgacem - Software Engineering graduate from the National Institute of Applied Sciences and Technology (INSAT) and  Artificial Intelligence, Systems, Data (IASD) master student at Paris Dauphine Tunis.](https://www.linkedin.com/in/ahmedbelgacem/)
- [Firas Meddeb - Business Administration graduate from Tunisian Business School and Artificial Intelligence, Systems, Data (IASD) master student at Paris Dauphine Tunis. ](https://www.linkedin.com/in/firasmeddeb/)
## Installation
```
pip install TunAugmentor
```
## Example
```python
from TunAugmentor.transformations import Flip,RandomRotation90,CenterCrop
from TunAugmentor.pipeline import Pipeline
from TunAugmentor.utils import read_images,export

Augmentor=Pipeline([Flip(V=-1,H=-1),RandomRotation90(),CenterCrop(300,300)])
images=read_images('./image_folder')
images=Augmentor.apply(images)
res=export(images,'./res')
```
##Transformation List
- ### CenterCrop:
- ### Crop:
- ### CropAndPad:
- ### CropOrPad:
- ### Flip:
- ### Flip Horizontal:
- ### Flip Vertical:
- ### Identity:
- ### Transpose:
- ### RandomCrop:
- ### RandomRotation90:

