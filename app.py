# API creation for submitting book reviews for NYTimes using Python, MongoDB, Flask, and HTML.
# Author: Gayatri Milind Hungund.
from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
from cryptography.fernet import Fernet
import secret
import helper

app = Flask(__name__)
api = Api(app)

#Simple first welcome page to showcase a link to documentation on API usage.
@app.route("/")
def hello():
    return render_template("home.html")

# HTTP GET method to retrieve book reviews for the user as per user request.
# The following GET method can retrieve aall book reviews or reviews for a particular book as per useer request.
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


# HTTP POST method to add a book review as per user input.
# the user enters 4 prameters namely: bookName, bookAuthor, bookReview, bookImage and data is inserted into MongoDB.
class BookReviews(Resource):
    def post(self):
        reviewList = list()
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("author")
        parser.add_argument("review")
        parser.add_argument("link")
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
