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

def convert_values2str(dig, dif_list):
    """
    convert features string to input of svm

    :param dig:
    :param dif_list:
    :return:
    """

    index = 1
    line = '%d' % (dig)

    for item in dif_list:
        fmt = ' %d:%d '% (index, item)
        line += fmt
        index += 1


    return line

def handle_train_file():

    """
    visit all train file get features

    :return:
    """

    TrainFolder = os.listdir('./ClassPic')

    SVMFeatureFile = './Feature.txt'
    SVMFeatureFileHandle = open(SVMFeatureFile, 'w')

    Label = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, \
             'a':10, 'a1':11, 'b':12, 'b1':13, 'c':14, 'c1':15, 'd':16, 'd1':17, 'e':18, 'e1':19, \
             'f':20, 'f1':21, 'g':22, 'g1':23, 'h':24, 'h1':25, 'i':26, 'i1':27, 'j':28, 'j1':29, \
             'k':30, 'k1':31, 'l':32, 'l1':33, 'm':34, 'm1':35, 'n':36, 'n1':37, 'o':38, 'o1':39, \
             'p':40, 'p1':41, 'q':42, 'q1':43, 'r':44, 'r1':45, 's':46, 's1':47, 't':48, 't1':49, \
             'u':50, 'u1':51, 'v':52, 'v1':53, 'w':54, 'w1':55, 'x':56, 'x1':57, 'y':58, 'y1':59, \
             'z':60, 'z1':61}

    for folder in TrainFolder:
        if folder == '.DS_Store':
            continue
        else:
            ClassFolder = os.listdir('./ClassPic/'+folder)

            for file in ClassFolder:
                if file == '.DS_Store':
                    continue
                else:
                    img = Image.open('./ClassPic/' + folder +'/' + file)
                    PixlCountList = get_featrue(img)

                    LabelImg = Label[folder]
                    Line = convert_values2str(LabelImg, PixlCountList)

                    SVMFeatureFileHandle.write(Line)
                    SVMFeatureFileHandle.write('\n')


def handle_test_file():
    """

    :return:
    """
    Label = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, \
             'a':10, 'a1':11, 'b':12, 'b1':13, 'c':14, 'c1':15, 'd':16, 'd1':17, 'e':18, 'e1':19, \
             'f':20, 'f1':21, 'g':22, 'g1':23, 'h':24, 'h1':25, 'i':26, 'i1':27, 'j':28, 'j1':29, \
             'k':30, 'k1':31, 'l':32, 'l1':33, 'm':34, 'm1':35, 'n':36, 'n1':37, 'o':38, 'o1':39, \
             'p':40, 'p1':41, 'q':42, 'q1':43, 'r':44, 'r1':45, 's':46, 's1':47, 't':48, 't1':49, \
             'u':50, 'u1':51, 'v':52, 'v1':53, 'w':54, 'w1':55, 'x':56, 'x1':57, 'y':58, 'y1':59, \
             'z':60, 'z1':61}

    TestFolder = os.listdir('./Test/ClassPic')

    SVMFeatureFile = './Test/Feature.txt'
    SVMFeatureFileHandle = open(SVMFeatureFile, 'w')

    for folder in TestFolder:
        if folder == '.DS_Store':
            continue
        else:
            ClassFolder = os.listdir('./Test/ClassPic/'+folder)

            for file in ClassFolder:
                if file == '.DS_Store':
                    continue
                else:
                    img = Image.open('./Test/ClassPic/' + folder +'/' + file)
                    PixlCountList = get_featrue(img)

                    LabelImg = Label[folder]
                    Line = convert_values2str(LabelImg, PixlCountList)

                    SVMFeatureFileHandle.write(Line)
                    SVMFeatureFileHandle.write('\n')



if __name__ == '__main__':

    handle_train_file()
