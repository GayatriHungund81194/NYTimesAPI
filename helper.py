import pymongo 
from pymongo.errors import ConnectionFailure, CollectionInvalid
import secret

def checkMongoConnectivity():
    try:
        mongoClient = pymongo.MongoClient("mongodb+srv://"+secret.mongoUser+":"+secret.mongoPassword+"@cluster0.cv48i.mongodb.net/NYTimes?retryWrites=true&w=majority")
    except ConnectionFailure:
        print("Failed to connect to database")
        return "Service Error: Unexpectd Error occured while processing your request HTTP 503 Service Unavailable"
    return mongoClient

def retriveAllBookReviews(collection):
    records = collection.find({},{"_id":0})
    reviewList = list()
    if records:
        for record in records:
            reviewList.append(record)
        print("Success: Request Successfull!! HTTP 200 OK")
        return reviewList
    else:
        print("No Records found")
        return "Response Error: No book reviews found on this website HTTP 404 Not Found"

def retrieveSpecificBookReviews(collection,bookName):
    records = collection.find({'name':bookName},{"_id":0})
    reviewList = list()
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

def checkParams(params):
    if (params==None or params['bookName']==None or params['bookAuthor'] or params['bookReview']==None or params['bookImage']==None):
        print("Bad Request: The name of request parameters should be as per documentation")
        return "Bad Request: Request parameter name not found HTTP 400 Bad Request"

def insertBookReview(collection,params):
    try:
        collection.insert_one(params)
        print("Data insertion successful")
        return "Success: Review Submitted Successfully!! HTTP 200 OK"
    except CollectionInvalid:
        print("Invalid Collection")
        return "Request Error: Could not query the collection. "