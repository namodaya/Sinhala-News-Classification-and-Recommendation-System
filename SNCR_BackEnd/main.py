from SNCR_BackEnd.Aggregator.hiruNews.HiruNewsAggregator import HirunNewsAggregator
from SNCR_BackEnd.Aggregator.deranaNews.DeranaNewsAggregator import DeranaNewsAggregator
from SNCR_BackEnd.Classifier.MNBclassifier import *
from SNCR_BackEnd.dao.DAO import *
from SNCR_BackEnd.Preprocessor.Prepocessing import *

dao = DAO()
preprocessor = Prepocessing()

latestNews = dao.selectLast('derananews')

aggrigater = DeranaNewsAggregator()
classifier = MultinomialNBClassifier()
list = aggrigater.aggriagteNews("http://sinhala.adaderana.lk/rsshotnews.php")

print 'latest news     ++++++'
print latestNews

for news in list:
    print news.publishDate
    if news.publishDate==latestNews:
        print 'Yes yes yes'

# for i in list:
#     print i.description
preprocessor.prepocessor(list)
# for i in list:
#     print i.description


classifier.classify(list)

for news in list:
    title = news.title
    newsSite = str(news.newsSite)
    category = news.category[0]
    link = news.link
    pubDate = str(news.publishDate)
    description = news.summary
    imgLink = news.imageLink
    dao.insertNews(title,link,description,imgLink,pubDate,category,newsSite)