# coding:utf8
import urllib.request
# import cookielib
import http.cookiejar

url = "http://www.baidu.com"

print("第一种方法")
response1 = urllib.request.urlopen(url)
print(response1.getcode())  # 返回状态码
print(len(response1.read()))  # 返回网页内容的长度

print("第二种方法")
request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print("第三种方法")
# cj = http.cookiejar()
# python错误TypeError: 'module' object is not callable 的解决方法
# 说明在把cookiejar模块当作函数来调用
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())  # 返回状态码
print(cj)  # 返回cookie
print(response3.read())  # 返回网页内容
