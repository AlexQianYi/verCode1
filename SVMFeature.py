import os
from os.path import join
from PIL import Image

def get_featrue(img):

    """
    get feature of img
    1. the feature of img is the sum of black pixel of every row and the sum of black pixel of every column
    2. sum result of row and column

    image size 22*34
    """



    width, height = img.size

    PixelCountList = []

    height = 34

    for y in range(height):
        PixelCountX = 0
        for x in range(width):
            if img.getpixel((x, y)) == 0:
                PixelCountX += 1

        PixelCountList.append(PixelCountX)

    for x in range(width):
        PixelCountY = 0
        for y in range(height):
            if img.getpixel((x, y)) == 0:
                PixelCountY += 1

        PixelCountList.append(PixelCountY)

    return PixelCountList


def get_svm_train_txt():

    """
    get
    
    """