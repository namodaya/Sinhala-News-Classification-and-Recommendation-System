from SNCR_BackEnd.Aggregator.news.NewsAggregator import NewsAggregator
aggrigater = NewsAggregator()

list = aggrigater.aggriagteNews("http://www.hirunews.lk/rss/sinhala.xml")

for i in list:
    print i.title