# -*- coding:utf-8 -*-
import sys
import urllib2
reload(sys)
sys.setdefaultencoding( "utf-8" )
from spider import *

html = etree.HTML(urllib2.urlopen("http://ssdut.dlut.edu.cn/index/bkstz.htm",timeout = 30).read().decode('utf-8'))
str = html.xpath('//li/a[@class="c56628"]/@href')

def make_url(string):
    url = 'http://ssdut.dlut.edu.cn'+string
    return url

def make_str(str):
    return str[2:]

urlList=[]
for i in range(len(str)):
    url=make_url(make_str(str[len(str)-i-1]))
    if url not in urlList:
        urlList.append(url)
        spider(url)
        f = open('/home/hc/PycharmProjects/dlut/xszz.txt', 'a')
        f.write('#############################################################################\n')
        f.close()
