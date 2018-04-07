#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://gist.github.com/chroman/5679049

# import the necessary packages
from PIL import Image
from PIL import ImageEnhance
import PIL.ImageOps
import pytesseract
import argparse
import cv2
import os
import numpy

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
args = vars(ap.parse_args())

print("args['image'] %s " % args["image"])

# load the example image and convert it to RGB, invert it and adjust brightness
image = Image.open(args["image"]).convert('RGB')
image = PIL.ImageOps.invert(image)
image = ImageEnhance.Brightness(image)
image = image.enhance(10)
imageArray = numpy.array(image)
imageArray = imageArray[:, :, ::-1].copy()

filename = "{}.png".format(os.getpid())
image.save(filename)


# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

# show the output images
cv2.imshow("Image", imageArray)
cv2.waitKey(0)

# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>python ocr.py -i 9393.png
# args['image'] 9393.png
# 9393

# (C:\Users\Han\Anaconda3) C:\Users\Han\selenium_test>python ocr.py -i test.jpg
# args['image'] test.jpg
# 1210 # jzj0
