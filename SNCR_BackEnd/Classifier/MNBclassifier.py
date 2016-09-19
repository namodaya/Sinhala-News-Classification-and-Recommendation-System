import io
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import os

from SNCR_BackEnd.Aggregator.news.News import *

class MultinomialNBClassifier:

    # Reading trining data files
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                           'Classifier\\newsGroups\\sport.txt'), 'r') as myfile:
        sport = myfile.read().replace('\n', '')

    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                           'Classifier\\newsGroups\\defence.txt'), 'r') as myfile:
        defence = myfile.read().replace('\n', '')

    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                           'Classifier\\newsGroups\\culture.txt'), 'r') as myfile:
        culture = myfile.read().replace('\n', '')

    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                           'Classifier\\newsGroups\\politics.txt'), 'r') as myfile:
        politics = myfile.read().replace('\n', '')

    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                           'Classifier\\newsGroups\\economy.txt'), 'r') as myfile:
        economy = myfile.read().replace('\n', '')

    def classifier(self, text):

        culture = self.culture
        sport = self.sport
        defence = self.defence
        economy = self.economy
        politics = self.politics

        #instantiate classifier and vectorizer
        clf=MultinomialNB(alpha=.01)
        vectorizer =TfidfVectorizer(min_df=1,ngram_range=(1,2))

        #Apply vectorizer to training data

        traindata=[sport,defence,economy,culture,politics];
        X_train=vectorizer.fit_transform(traindata)

        #Label Ids
        # sport = 0
        # defence = 1
        # economy = 2
        # culture = 3
        # politics = 4
        y_train=[0,1,2,3,4];

        #Train classifier
        clf.fit(X_train, y_train)


        return clf.predict(vectorizer.transform([text]))

    def classify(self, newsList):

        for news in newsList:
            description = news.title
            # print description
            # wf = io.open(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Classifier\\newsGroups\\news.txt'), 'w')
            # x = unicode(description, "utf-8")
            # wf.write('zzzzzzzz')
            # wf.close()
            # rf = io.open(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'Classifier\\newsGroups\\news.txt'), 'r', encoding='utf-8').read()
            category = MultinomialNBClassifier().classifier(description)

            print category,description

            news.category = category

        # return newsList
