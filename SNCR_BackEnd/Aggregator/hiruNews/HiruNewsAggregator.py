import urllib2
from bs4 import BeautifulSoup

import re

from SNCR_BackEnd.Aggregator.news.NewsAggregator import NewsAggregator

class HirunNewsAggregator(NewsAggregator):

    def setDescription(self, news, entry):
        url = entry['link']
        content = urllib2.Request(url)
        res = urllib2.urlopen(content).read()
        try:
            soup = BeautifulSoup(res, "html.parser")
        except:
            print "Error"
        description = soup.find_all(True, attrs={"class": "lts-txt2"})
        news.description = description
        print "description sussefully fetched"

    def setLink(self, news, entry):
        url = entry['link']
        news.link = url+'/'+news.title.replace(" ", "")
        print "news link sussefully fetched"

    def setNewsSite(self, news):
        news.newsSite = "HiruNews"
        print "news site sussefully fetched"

    def setImageLink(self, news, entry):
        url = entry['link']
        content = urllib2.Request(url)
        res = urllib2.urlopen(content).read()
        try:
            soup = BeautifulSoup(res, "html.parser")
        except:
            print "Error"
        imgsrc = soup.find_all(True, attrs={"class": "latest-pic"})
        patImgSrc = re.compile('src="(.*)".*/>')
        findPatImgSrc = re.findall(patImgSrc, str(imgsrc))
        news.imageLink = findPatImgSrc[0]
        print "image link sussefully fetched"

    def setSummary(self, news, entry):
        summary = entry['description']
        summaryArray = summary.split("<")
        news.summary = summaryArray[0]
        print news.summary
        print "summary sussefully fetched"



