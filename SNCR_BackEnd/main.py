from SNCR_BackEnd.Aggregator.news.NewsAggregator import NewsAggregator
from SNCR_BackEnd.Classifier.MNBclassifier import *
from SNCR_BackEnd.dao.DAO import *

dao = DAO()

dao.selectLast('hirunews')

aggrigater = NewsAggregator()
classifier = MultinomialNBClassifier()
list = aggrigater.aggriagteNews("http://www.hirunews.lk/rss/sinhala.xml")

for i in list:
    print i.category

classifier.classify(list)

for i in list:
    print i.category
