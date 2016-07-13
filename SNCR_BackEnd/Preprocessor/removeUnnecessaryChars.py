import re

from mysql.connector import (connection)

db = connection.MySQLConnection(user='root', password='1234',
                                host='127.0.0.1',
                                database='NewsData',
                                charset='utf8')

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT title FROM NewsOrder"
cursor.execute(sql)
title = cursor.fetchall()

cyril = re.compile(u"[\u0021-\u007F]+", re.UNICODE)
# plainText = cyril.sub('',news)
#
# print plainText

for row in title:
    plainText = cyril.sub('', row[0])
    print plainText