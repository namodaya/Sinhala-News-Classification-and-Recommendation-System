import schedule
import time

from SNCR_BackEnd.configSectionMap import *
from newsUpdater import *

configSectionMap = ConfigSectionMap()

link = configSectionMap.ConfigSectionMap("HiruNews")['link']
newsContentClassName = configSectionMap.ConfigSectionMap("HiruNews")['newscontentclassname']
imageClassName = configSectionMap.ConfigSectionMap("HiruNews")['imageclassname']

newsUpdater = newsUpdater()
schedule.every(0.5).minutes.do(newsUpdater.job,link,newsContentClassName, imageClassName)

while 1:
    schedule.run_pending()
    time.sleep(0.5)