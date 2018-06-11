from spider import downimage
from binImg import *
from cutImg import *




if __name__ == "__main__":

    print('input the number of test pictures...')
    TestPicNum = int(input())

    """
    Download i test images in file Test/OriginPic
    """
    for i in range(TestPicNum):
        downimage(i, "./Test/OriginPic/" + str(i) + "image.jpg")
        print('Download test image: ' + str(i) + ' in Test/OriginPic')
    print('------------------------------------------------------')
    print('--------------------Download Finish-------------------')
    print('------------------------------------------------------')
    print('-------------------Get Binary Image-------------------')

    """
    get Binary version of images
    """
    images = os.listdir('./Test/OriginPic')
    BinImgDes = './Test/BinPic/'
    count1 = 0
    for file in images:
        imgName = file[:-9]
        print('Handle image: ' + imgName + ' No.' + str(count1))
        img = Image.open('./Test/OriginPic/'+file)
        binImg = binImage(img)

        binImgName = BinImgDes + imgName + 'image.jpg'
        binImg.save(binImgName)
        count1 += 1
    print('------------------------------------------------------')
    print('-----------------Binaryzation Finish------------------')
    print('------------------------------------------------------')
    print('---------------------Cut Images-----------------------')

    """
    Cut Images to 5
    """

    BinImage = os.listdir('./Test/BinPic')
    count2 = 0
    CutImgDes = './Test/CutPic/'
    for file in BinImage:
        imgNum = file[:-9]
        print('Cut image: ' + imgName + ' No.' + str(count2))

        img = Image.open('./BinPic/' + file)

        ChildImgList = get_children_img(img)
        save_children_img(imgNum, ChildImgList, CutImgDes)

        count2 += 1
    print('------------------------------------------------------')
    print('--------------------Cut Image Finish------------------')
    print('------------------------------------------------------')
    print('------------------Generate SVM Vector-----------------')

    """
    get test image feature
    """
















