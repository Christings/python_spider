# coding:utf-8

from basicspider.DataOutput import DataOutput
from basicspider.HtmlDownloader import HtmlDownloader
from basicspider.HtmlParser import HtmlParser
from basicspider.URLManager import UrlManager


class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self,root_url):
        # 添加入口URL
        self.manager.add_new_url(root_url)
        # 判断url管理器中是否有新的url，同时判断抓取了多少个url