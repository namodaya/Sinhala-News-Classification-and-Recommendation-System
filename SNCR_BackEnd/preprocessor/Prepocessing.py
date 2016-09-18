import io
import os

from SNCR_BackEnd.preprocessor.removingStopWords.RemovingStopWords import RemovingStopWords
from SNCR_BackEnd.preprocessor.removingUnnecessaryChars.removeUnnecessaryChars import removeUnnecessaryChars
from SNCR_BackEnd.preprocessor.stemming.StemmingSinhala import StemmingSinhala

class Prepocessing():

    def prepocessor(self,description):

        unnecessaryCharsObj = removeUnnecessaryChars()
        stopWrdsObj = RemovingStopWords()
        stemmObj = StemmingSinhala()

        text = unnecessaryCharsObj.removeChars(description)
        text = stopWrdsObj.removeStopwords(text)

        text = text.lower()
        plain = text.split()
        stemmObj.stemminig(plain)

        plainText=""

        for x in plain:
            plainText = plainText+" "+x

        return plainText
