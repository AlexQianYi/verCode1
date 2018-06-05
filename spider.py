# coding:utf8
import requests

"""
download dataset
"""

def downimage(i):
    # 构建session
    sess = requests.Session()
    # 建立请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
        "Connection": "keep-alive"}
    url = "https://account.flycua.com/sso/chineseVerifyCode.images"
    # 获取响应图片内容
    image = sess.get(url, headers=headers).content
    # 保存到本地
    with open("./VerPic/" + str(i) + "image.jpg", "wb") as f:
        f.write(image)


if __name__ == "__main__":
    for i in range(1000):
        print('正在下载: ',i+1)
        downimage(i)
