from SNCR_BackEnd.Aggregator.deranaNews.DeranaNewsAggregator import DeranaNewsAggregator
from SNCR_BackEnd.Aggregator.hiruNews.HiruNewsAggregator import HirunNewsAggregator

# hiruAggrigator = HirunNewsAggregator()
# list = hiruAggrigator.aggriagteNews("http://www.hirunews.lk/rss/sinhala.xml")

deranaAggrigator = DeranaNewsAggregator();
list = deranaAggrigator.aggriagteNews("http://sinhala.adaderana.lk/rsshotnews.php")

for i in list:
    print i.summary