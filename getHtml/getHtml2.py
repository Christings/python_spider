#coding=utf-8
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    print(html)
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html.decode('utf-8'))
    x = 0
    print("start download pic")
    for imgurl in imglist:
        print(imgurl)
        #urllib.request.urlretrieve(imgurl,'D:\\taiyan\\'+'%s.jpg'%x) #把数据保存在D盘taiyan文件夹下
        urllib.request.urlretrieve(imgurl,'%s.jpg'%x)  #把数据保存在代码的文件夹下，urlretrieve的python3的位置也变了，多了request
        x+=1
    print("done")


html = getHtml("http://tieba.baidu.com/p/2460150866")

print(getImg(html))