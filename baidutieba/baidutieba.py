# -*- coding:utf-8 -*-
import urllib.request
import urllib.error
import re


# 百度贴吧爬虫类
class BDTB:
    # 初始化，传入基地址，是否只看楼主的参数
    def __init__(self, baseUrl, seeLZ):
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz' + str(seeLZ)

    # 传入页码，获取该页帖子的代码
    def getPage(self, pageNum):
        try:
            url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            print(response.read())
            return response
        except urllib.error.URLError as e:
            if hasattr(e, "reason"):
                print(u"连接百度贴吧失败，错误原因：", e.reason)
                return None

    # 获取帖子标题
    def getTitle(self):
        page = self.getPage(1)
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h1>', re.S)
        result = re.search(pattern, page)
        if result:
            print(result.group(1))  # 测试输出
            return result.group(1).strip()
        else:
            return None


baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL, 1)
bdtb.getPage(1)
