from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img_path = './verPic/1image.jpg'


"""
binary image grey
pixel>threshold = 1 else 0
"""
def binImage(img_path, threshold=140):
    img = np.array(Image.open(img_path).convert('L'))


    rows, cols = img.shape
    for i in range(rows):
        for j in range(cols):
            if (img[i, j] <= threshold):
                img[i, j] = 0
            else:
                img[i, j] = 1

    img_result = img
    for i in range(rows):
        for j in range(cols):
            if sumNei(img, i, j) < 3:
                img_result[i, j] = 0

    plt.imshow(img, cmap='gray')
    plt.show()

# def removeNoise(imgArray):

def sumNei(img, x, y):

    curPixel = img.getpixel((x, y))
    width = img.width
    height = img.height

    if curPixel==0: # white
        return 0

    if y == 0:      # 1st row
        if x==0:    # topleft corner
            sum = curPixel \
                + img.getpixel((x, y+1)) \
                + img.getpixel((x+1, y)) \
                + img.getpixel((x+1, y+1))
            return 4-sum

        elif x == width - 1:    #bottomright corner
            sum = curPixel \
                + img.getpixel((x, y+1)) \
                + img.getpixel((x-1, y)) \
                + img.getpixel((x-1, y+1))
            return 4-sum
        else:
            sum = img.getpixel((x-1, y)) \
                + img.getpixel((x-1, y+1)) \
                + curPixel \
                + img.getpixel((x, y+1)) \
                + img.getpixel((x+1, y)) \
                + img.getpixel(x+1, y+1)
            return 6-sum
    elif y==height-1:       # bottom row
        if x==0:            # bottomleft
            sum = curPixel \
                + img.getpixel((x+1, y)) \
                + img.getpixel((x+1, y-1)) \
                + img.getpixel((x, y-1))
            return 4-sum

        elif x == width-1:  # bottomright
            sum = curPixel \
                + img.getpixel((x, y-1)) \
                + img.getpixel((x-1, y)) \
                + img.getpixel((x, y-1))
            return 4-sum
        else:
            sum = curPixel \
                + img.getpixel((x-1, y)) \
                + img.getpixel((x+1, y)) \
                + img.getpixel((x, y-1)) \
                + img.getpixel((x-1, y-1)) \
                + img.getpixel((x+1, y-1))
            return 6-sum

    else:
        if x==0:    # left edge
            sum = img.getpixel((x, y-1)) \
                + curPixel \
                + img.getpixel((x, y+1)) \
                + img.getpixel((x+1, y-1)) \
                + img.getpixel((x+1, y)) \
                + img.getpixel((x+1, y+1))
            return 6-sum

        elif x == width - 1:    # right edge
            sum = img.getpixel((x, y-1)) \
                + curPixel \
                + img.getpixel((x, y+1)) \
                + img.getpixel((x-1, y-1)) \
                + img.getpixel((x-1, y)) \
                + img.getpixel((x-1, y+1))
            return 6-sum

        else:
            sum = img.getpixel((x-1, y-1)) \
                + img.getpixel((x-1, y)) \
                + img.getpixel((x-1, y+1)) \
                + img.getpixel((x, y-1)) \
                + curPixel \
                + img.getpixel((x, y+1)) \
                + img.getpixel((x+1, y-1)) \
                + img.getpixel((x+1, y)) \
                + img.getpixel((x+1, y+1))
            return 9-sum

if __name__ == '__main__':

    img = Image.open(img_path).convert('L')

    binImage(img_path)
