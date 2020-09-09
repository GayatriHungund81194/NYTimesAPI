from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import random
import pymongo 
from pymongo.errors import ConnectionFailure, CollectionInvalid
import secret
import helper

app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return render_template("home.html")
class Books(Resource):
    def get(self):
        reviewList = list()
        parser = reqparse.RequestParser()
        parser.add_argument("bookName")
        params = parser.parse_args()
        mongoClient = helper.checkMongoConnectivity()      
        try:
            db = mongoClient['NYTimes']
            collection = db['BookReview']
        except CollectionInvalid:
            print("Invalid Collection")
            return "Request Error: Could not query the collection. "
        
        if (params['bookName'] is None):
            return helper.retriveAllBookReviews(collection)
        else:
            return helper.retrieveSpecificBookReviews(collection,params['bookName'])
        return "Unexpectd Error Occured! Pleaase try again later"

api.add_resource(Books,"/getBooks","/getBooks")

class BookReviews(Resource):
    def post(self):
        reviewList = list()
        parser = reqparse.RequestParser()
        parser.add_argument("bookName")
        parser.add_argument("bookAuthor")
        parser.add_argument("bookReview")
        parser.add_argument("bookImage")
        params = parser.parse_args()
        print(params)
        paramCheck = helper.checkParams(params)
        if paramCheck:
            mongoClient = helper.checkMongoConnectivity()
            db = mongoClient['NYTimes']
            collection = db['BookReview'] 
            return helper.insertBookReview(collection,params)
        return "Unexpectd Error Occured! Pleaase try again later"
        
api.add_resource(BookReviews,"/addReview","/addReview")

if __name__ == '__main__':
    app.run(debug=True)
