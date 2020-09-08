from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import pymongo 
from pymongo.errors import ConnectionFailure, CollectionInvalid


app = Flask(__name__)
api = Api(app)

class Books(Resource):
    def get(self):
        reviewList = list()
        parser = reqparse.RequestParser()
        parser.add_argument("bookName")
        params = parser.parse_args()
        if (params==None):
            print("Bad Request: The name of request parameters should be as per documentation")
            return "Bad Request: Request parameter name not found HTTP 400 Bad Request"
        print("Params",params['bookName'])        
        try:
            mongoClient = pymongo.MongoClient("localhost",27017)
        except ConnectionFailure:
            print("Failed to connect to database")
            return "Service Error: Unexpectd Error occured while processing your request HTTP 503 Service Unavailable"
        try:
            db = mongoClient['NYTimes']
            collection = db['BookReview']
        except CollectionInvalid:
            print("Invalid Collection")
            return "Request Error: Could not query the collection. "
        if (params['bookName'] is None):
            print("in if loop")
            records = collection.find({},{"_id":0})
            if records:
                for record in records:
                    reviewList.append(record)
                print("Success: Request Successfull!! HTTP 200 OK")
                return reviewList
            else:
                print("No Records found")
                return "Response Error: No book reviews found on this website HTTP 404 Not Found"
        else:
            print("in else loop")
            records = collection.find({'name':params['bookName']},{"_id":0})
            print(records)
            if records:
                for record in records:
                    reviewList.append(record)
                    print(reviewList)
                print("Success: Request Successfull!! HTTP 200 OK")
                return reviewList
            else:
                print("No Records found")
                return "Response Error: No book reviews found on this website HTTP 404 Not Found"
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
        if (params==None or params['bookName']==None or params['bookAuthor'] or params['bookReview']==None or params['bookImage']==None):
            print("Bad Request: The name of request parameters should be as per documentation")
            return "Bad Request: Request parameter name not found HTTP 400 Bad Request"
        try:
            mongoClient = pymongo.MongoClient("localhost",27017)
        except ConnectionFailure:
            print("Failed to connect to database")
            return "Service Error: Unexpectd Error occured while processing your request HTTP 503 Service Unavailable"
        try:
            db = mongoClient['NYTimes']
            collection = db['BookReview']
            collection.insert_one(params)
            print("Data insertion successful")
            return "Success: Review Submitted Successfully!! HTTP 200 OK"
        except CollectionInvalid:
            print("Invalid Collection")
            return "Request Error: Could not query the collection. "
        return "Unexpectd Error Occured! Pleaase try again later"
        
api.add_resource(BookReviews,"/addReview","/addReview")

if __name__ == '__main__':
    app.run(debug=True)
