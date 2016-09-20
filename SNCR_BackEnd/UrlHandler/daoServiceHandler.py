import feedparser
from flask_restful import Resource
from SNCR_BackEnd.dao.DAO import DAO


class daoServiceHandler(Resource):
    def get(self, Category):
        dao = DAO()

        if (Category=='hotNews'):
            print "fetching hot news"
            news = dao.getHotNews()
        else:
            if(Category=='defence'):
                print "fetching defence and law news"
                news = dao.getNews("defence")
            else:
                if (Category == 'culture'):
                    print "fetching art and culture news"
                    news = dao.getNews("culture")
                else:
                    if (Category == 'political'):
                        print "fetching political news"
                        news = dao.getNews("political")
                    else:
                        if (Category == 'economics'):
                            print "fetching business and economics  news"
                            news = dao.getNews("economics")
                        else:
                            if (Category == 'sports'):
                                print "fetching sport news"
                                news = dao.getNews("sports")


        newsList = []

        print news
        # print the rows
        for row in news:
            spltDescription = unicode(row[3]).split("<a")
            newsList.append({
                'title': row[1],
                'link': row[2],
                'description': spltDescription[0],
                'image': row[4],
                'articleId': row[6]

            })

        return (newsList)

