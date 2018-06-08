import requests
from spider import downimage




if __name__ == "__main__":

    print('input the number of test pictures...')
    TestPicNum = int(input())
    """
    Download i test images in file Test/OriginPic
    """

    for i in range(TestPicNum):
        downimage(i, ".Test/OriginPic/" + str(i) + "image.jpg")
        print('Download test image: ' + str(i) + 'in Test/OriginPic')







