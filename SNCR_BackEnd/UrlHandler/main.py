import os
from dns.message import make_response
from httplib2 import Http

import flask
from flask_restful import Api
from flask.ext.cors import CORS
from flask import session


from SNCR_BackEnd.UrlHandler.daoServiceHandler import daoServiceHandler
from werkzeug.contrib.jsrouting import render_template

app = flask.Flask(__name__)
app.secret_key = os.urandom(24)
api = Api(app)
CORS(app)
api.add_resource(daoServiceHandler, '/category/<string:Category>', endpoint='/')
# api.add_resource(Login, '/login')
# api.add_resource(userData, '/userHistory')

# def get_user_data(access_token):
#     headers = {'Content-Type': 'text/html'}
#     parser = Http()
#     resp, content = parser.request("https://www.googleapis.com/oauth2/v1/userinfo?access_token={accessToken}".format(
#         accessToken=access_token))
#     # this gets the google profile!!
#     print content
#     return make_response(
#         render_template('home.html',
#                         content=content
#                         ),
#         200, headers
#     )

# @app.route('/callback')
# @google.authorized_handler
# def authorized(resp):
#     session['access_token'] = resp['access_token']
#     return get_user_data(session["access_token"])
#
# @google.tokengetter
# def get_access_token():
#     return session.get('access_token')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)