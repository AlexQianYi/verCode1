from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

img_path = './verPic/1image.jpg'
file_origin = './VerPic'
file_destin = './BinPic'


"""
binary image grey
pixel>threshold = 1 else 0
"""
def binImage(image):
    imgry = image.convert('L')

    table = get_bin_table()
    out = imgry.point(table, '1')

    noise_list = []
    for i in range(out.width):
        for j in range(out.height):
            num9 = sumNei(out, i, j)
            if num9<3 and out.getpixel((i, j)) ==0:
                pos = (i, j)
                noise_list.append(pos)

    remove_noise_pixel(out, noise_list)
    return out


def get_bin_table(threshold=170):
    table = []
    for i in range(256):
        if i<threshold:
            table.append(0)
        else:
            table.append(1)
    return table

def remove_noise_pixel(img, noise_list):

    for item in noise_list:
        img.putpixel((item[0], item[1]), 1)


def sumNei(img, x, y):

    curPixel = img.getpixel((x, y))

    width = img.width
    height = img.height

    if curPixel==1: # white
        return 0

    if y == 0:  # 第一行
        if x == 0:  # 左上顶点,4邻域
            # 中心点旁边3个点
            sum = curPixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 4 - sum
        elif x == width - 1:  # 右上顶点
            sum = curPixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 4 - sum
        else:  # 最上非顶点,6邻域
            sum = img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + curPixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 6 - sum
    elif y == height - 1:  # 最下面一行
        if x == 0:  # 左下顶点
            # 中心点旁边3个点
            sum = curPixel \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x, y - 1))
            return 4 - sum
        elif x == width - 1:  # 右下顶点
            sum = curPixel \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y - 1))

            return 4 - sum
        else:  # 最下非顶点,6邻域
            sum = curPixel \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x, y - 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x + 1, y - 1))
            return 6 - sum
    else:  # y不在边界
        if x == 0:  # 左边非顶点
            sum = img.getpixel((x, y - 1)) \
                  + curPixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))

            return 6 - sum
        elif x == width - 1:  # 右边非顶点
            # print('%s,%s' % (x, y))
            sum = img.getpixel((x, y - 1)) \
                  + curPixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1))

            return 6 - sum
        else:  # 具备9领域条件的
            sum = img.getpixel((x - 1, y - 1)) \
                  + img.getpixel((x - 1, y)) \
                  + img.getpixel((x - 1, y + 1)) \
                  + img.getpixel((x, y - 1)) \
                  + curPixel \
                  + img.getpixel((x, y + 1)) \
                  + img.getpixel((x + 1, y - 1)) \
                  + img.getpixel((x + 1, y)) \
                  + img.getpixel((x + 1, y + 1))
            return 9 - sum


if __name__ == '__main__':


    count = 0

    names = os.listdir(file_origin)


    for file in names:
        fileNum = file[:-9]
        info = "handle " + str(count+1) + "pic: " + fileNum
        print(info)

        img = Image.open('./VerPic/' + file).convert('L')

        binImg = binImage(img)

        file_dest = "./BinPic/" + fileNum + "image.jpg"
        binImg.save(file_dest)
        count += 1



