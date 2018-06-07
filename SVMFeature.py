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
    get feature file of test dataset

    """

    SVMFeatureFile = open(TrainFileName, 'w')

    LabelList = ['0', '1', '2', '3']

    for i in range(len(LabelList)):
        ImgFolder = join(CutPicFolder, str(i))
        CovertImgs2FeatureFile(i, SVMFeatureFile, ImgFolder)


    SaveFeatureFile.close()


def get_svm_test_txt():

    """
    get test file
    :return:
    """

    ImgFolder = TestCutPicFolder
    TestFile = open(TestFeatureFile, 'w')


def covert_imgs2feature_file(dig, svm_feature_file, img_folder):
    """

    covert img in img_folder to feature file
    :param dig: check number
    :param svm_feature_file: svm feature file
    :param img_folder:
    :return:
    """


    FileList = os.listdir(img_folder)


    for file in FileList:
        img = Image.open(img_folder + '/' + file)
        DifList = get_featrue(img)

        Line = conver_values2str(dig, DifList)
        svm_feature_file.write(line)
        svm_feature_file.write('\n')

def convert_values_to_str(dig, dif_list):
    """
    convert features string to input of svm

    :param dig:
    :param dif_list:
    :return:
    """

    index = 1
    line = '%d' % dig

    for item in dif_list:
        fmt = ' %d:%d '% (index, item)
        line += fmt
        index += 1


    return line


def convert_feature2vector(feature_list):

    """

    :param feature_list:
    :return:
    """

    index = 1
    xtVector = []
    feature_dict = {}

    for item in feature_list:

        feature_dict[index] = item
        index += 1
    xtVector.append(feature_dict)
    return xtVector

if __name__ == '__main__':
    