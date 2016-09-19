from SNCR_BackEnd.Aggregator.hiruNews.HiruNewsAggregator import HirunNewsAggregator
from SNCR_BackEnd.Classifier.MNBclassifier import *
from SNCR_BackEnd.dao.DAO import *

dao = DAO()

dao.selectLast('hirunews')

aggrigater = HirunNewsAggregator()
classifier = MultinomialNBClassifier()
list = aggrigater.aggriagteNews("http://www.hirunews.lk/rss/sinhala.xml")

for i in list:
    print i.description

classifier.classify(list)

for i in list:
    print i.category
