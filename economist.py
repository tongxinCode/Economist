# -*- coding: utf-8 -*-
import os
import sys
import urllib2
import requests
import re
from lxml import etree
from apitranslator import requests_for_dst

def StringListSave(save_path, filename, slist):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    path = save_path+"/"+filename+".txt"
    with open(path, "w+") as fp:
        for s in slist:
            fp.write("%s\n%s\n%s\n%s\nhttps://www.economist.com%s\n\n" % (requests_for_dst(s[0]).encode("utf8"),\
             s[0].encode("utf-8"),requests_for_dst(s[1]).encode("utf8"),s[1].encode("utf-8"),s[2].encode("utf8")))

def Page_Info(myPage):
	dom=etree.HTML(myPage)
	sub_title=dom.xpath('//div/article/a/div/h3/span[1]/text()')
	main_title=dom.xpath('//div/article/a/div/h3/span[2]/text()')
	article_href=dom.xpath('//div/article/a/@href')
	return zip(sub_title,main_title,article_href)


def Spider(url):
	print "downloading ",url
	myPage = requests.get(url).content.decode("utf8")
	myPageResults = Page_Info(myPage)
	save_path=u"the_economist"
	filename=u"hotnews"
	StringListSave(save_path, filename, myPageResults)

if __name__ == '__main__':
	print "start"
	spider_url="https://www.economist.com/"
	Spider(spider_url)
	print "end"