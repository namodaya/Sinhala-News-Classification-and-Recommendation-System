import feedparser
from flask_restful import Resource

from mysql.connector import (connection)


class main(Resource):
    def get(self, Category):
        db = connection.MySQLConnection(user='root', password='ilovepera',
                                         host='127.0.0.1',
                                         database='NewsData',
                                         charset='utf8')

        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        print Category

        if (Category=='hotNews'):
            sql = "SELECT * FROM NewsOrder"
        else:
            sql = "SELECT * FROM NewsOrder WHERE category = '%s'"%(Category);


        cursor.execute(sql)
        news = cursor.fetchall()
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

        db.close()
        return (newsList)

