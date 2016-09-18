from abc import abstractmethod

import feedparser

from SNCR_BackEnd.Aggregator.news.News import News


class NewsAggregator:

    newsList = [News];

    def setTitle(self,news,entry):
        title = entry['title']
        news.title = title
        return news

    def setLink(self,news,entry):
        url = entry['link']
        news.link = url
        return news

    @abstractmethod
    def setDescription(self, news):
        pass

    @abstractmethod
    def imageLink(self, news):
        pass

    @abstractmethod
    def setPublishDate(self, news):
        pass

    @abstractmethod
    def setNewsSite(self, news):
        pass

    def aggriagteNews(self,link):

        aggrigater = NewsAggregator()
        print("Scheduler is running.......")
        feed = feedparser.parse(link)
        for entry in feed['items']:
            news = News()
            aggrigater.setTitle(news,entry)

            aggrigater.newsList.append(news)

        return aggrigater.newsList


