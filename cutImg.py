from PIL import Image
import os

file_origin = './BinPic'

def get_children_img(img):

    ChildImgList = []

    for i in range(5):
        x = 9 + i * (22+8)
        y = 9
        ChildImg = img.crop((x, y, x+22, y+34))
        ChildImgList.append(ChildImg)

    return ChildImgList

def save_children_img(path, ChildImgList):

    FullFileName = os.path.basename(path)
    FullFileNameSplit = FullFileName.split('.')
    FileName = FullFileNameSplit[0]

    i = 0
    for ChildImg in ChildImgList:
        CutImgFileName = FileName + '-' + ("%s.jpg" % i)
        ChildImg.save("./CutPic/" + CutImgFileName)

        i+=1

if __name__ == "__main__" :

    count = 0
    names = os.listdir(file_origin)


    for file in names:
        fileNum = file[:-9]
        info = "cut " + str(count+1) + "pic : " + fileNum
        print(info)

        img = Image.open('./BinPic/' + file).convert('L')

        ChildImgList = get_children_img(img)
        save_children_img(fileNum, ChildImgList)

        count += 1

    img = Image.open('82image.jpg')

    ChildImgList = get_children_img(img)

    save_children_img('82image.jpg', ChildImgList)

