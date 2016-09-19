import urllib2
from bs4 import BeautifulSoup
import re

from SNCR_BackEnd.Aggregator.news.NewsAggregator import NewsAggregator

class DeranaNewsAggregator(NewsAggregator):

    def setDescription(self, news, entry):
        url = entry['link']
        content = urllib2.Request(url)
        res = urllib2.urlopen(content).read()
        try:
            soup = BeautifulSoup(res, "html.parser")
        except:
            print "Error"
        description = soup.find_all(True, attrs={"class": "newsContent"})
        news.description = description[0]
        print "description sussefully fetched"

    def setNewsSite(self, news):
        news.newsSite = "DeranaNews"
        print "news site sussefully fetched"

    def setImageLink(self, news, entry):
        url = entry['link']
        content = urllib2.Request(url)
        res = urllib2.urlopen(content).read()
        try:
            soup = BeautifulSoup(res, "html.parser")
        except:
            print "Error"

        imgsrc = soup.find_all(True, attrs={"class": "img-responsive"})
        patImgSrc = re.compile('src="(.*)".*/>')
        findPatImgSrc = re.findall(patImgSrc, str(imgsrc[5]))
        news.imageLink = findPatImgSrc[0]
        print "image link sussefully fetched"


