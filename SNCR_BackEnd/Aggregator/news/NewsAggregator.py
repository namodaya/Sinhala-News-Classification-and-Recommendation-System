from abc import abstractmethod

import feedparser

from SNCR_BackEnd.Aggregator.news.News import News


class NewsAggregator:

    newsList = [News];

    def setTitle(self,news,entry):
        title = entry['title']
        news.title = title
        print "title sussefully fetched"

    @abstractmethod
    def setLink(self,news,entry):
        url = entry['link']
        news.link = url
        return news

    @abstractmethod
    def setSummary(self, news, entry):
        summary = entry['description']
        summaryArray = summary.split("<")
        news.summary = summaryArray[0]
        print "summary sussefully fetched"

    @abstractmethod
    def setDescription(self, news,entry):
        pass

    @abstractmethod
    def setImageLink(self, news,entry):
        pass

    @abstractmethod
    def setNewsSite(self, news):
        pass

    def setPublishDate(self, news,entry):
        date = entry['published']
        news.publishDate = date
        print "publish date sussefully fetched"

    def aggriagteNews(self,link):

        print("Scheduler is running.......")
        feed = feedparser.parse(link)
        for entry in feed['items']:
            news = News()
            self.setTitle(news,entry)
            self.setLink(news,entry)
            self.setSummary(news,entry)
            self.setDescription(news, entry)
            self.setImageLink(news, entry)
            self.setNewsSite(news)
            self.setPublishDate(news, entry)

            self.newsList.append(news)

        return self.newsList


