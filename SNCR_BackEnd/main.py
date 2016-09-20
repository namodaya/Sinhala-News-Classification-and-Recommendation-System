import rfc822
import schedule
import time

from SNCR_BackEnd.Aggregator.hiruNews.HiruNewsAggregator import HirunNewsAggregator
from SNCR_BackEnd.Aggregator.deranaNews.DeranaNewsAggregator import DeranaNewsAggregator
from SNCR_BackEnd.Classifier.MNBclassifier import *
from SNCR_BackEnd.dao.DAO import *
from SNCR_BackEnd.Preprocessor.Prepocessing import *

dao = DAO()
preprocessor = Prepocessing()

def schedularRunner():
    latestNews = dao.selectLast('derananews')

    print latestNews

    aggrigater = DeranaNewsAggregator()
    classifier = MultinomialNBClassifier()

    list = aggrigater.aggriagteNews("http://sinhala.adaderana.lk/rsshotnews.php")

    latestNewsList = [News]

    for news in list:
        if rfc822.parsedate_tz(news.publishDate) == rfc822.parsedate_tz(latestNews):
            break
        else:
            latestNewsList.append(news)

    preprocessor.prepocessor(latestNewsList)

    classifier.classify(latestNewsList)

    for news in latestNewsList:

        title = news.title
        newsSite = str(news.newsSite)
        category = news.category[0]
        link = news.link
        pubDate = str(news.publishDate)
        description = news.summary
        imgLink = news.imageLink
        if description != '':
            dao.insertNews(title, link, description, imgLink, pubDate, category, newsSite)


schedule.every(1).minutes.do(schedularRunner)

while 1:
    schedule.run_pending()
    time.sleep(0.1)