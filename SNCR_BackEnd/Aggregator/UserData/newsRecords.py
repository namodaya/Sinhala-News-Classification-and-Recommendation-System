from flask_restful import Resource, request

class userData(Resource):
    def post(self):
        print request.form['lak']