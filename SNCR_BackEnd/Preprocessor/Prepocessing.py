from SNCR_BackEnd.Preprocessor.removingStopWords.RemovingStopWords import RemovingStopWords
from SNCR_BackEnd.Preprocessor.removingUnnecessaryChars.removeUnnecessaryChars import removeUnnecessaryChars
from SNCR_BackEnd.Preprocessor.stemming.StemmingSinhala import StemmingSinhala

class Prepocessing():

    def prepocessor(self,newsList):

        for news in newsList:

            description = news.description

            unnecessaryCharsObj = removeUnnecessaryChars()
            stopWrdsObj = RemovingStopWords()
            stemmObj = StemmingSinhala()

            reomveCharsText = unnecessaryCharsObj.removeChars(description)
            # removeStopWordText = stopWrdsObj.removeStopwords(reomveCharsText)
            #
            # text = reomveCharsText.lower()
            # plain = text.split()
            # stemmObj.stemminig(plain)
            #
            # plainText=""
            #
            # for x in plain:
            #     plainText = plainText+" "+x

            news.description = reomveCharsText

        return newsList