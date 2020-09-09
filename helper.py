# API creation for submitting book reviews for NYTimes using Python, MongoDB, Flask, and HTML.
# This is a helper utulity designd to promote code modularity containing crucial methods used for proper functioning of API.
# Author: Gayatri Milind Hungund
import pymongo 
from pymongo.errors import ConnectionFailure, CollectionInvalid
from cryptography.fernet import Fernet
import secret


# The following method checks the connectivity to remote cloud MongoDB cluster and throws error in case of connection problems.
def checkMongoConnectivity():
    uname = bytes(secret.mongoUser, 'utf-8')
    key = bytes("xJoZAbtudAAnDnm8FBh-d3pIvTEargxQNpbb6JFiZ1g=", 'utf-8')
    enc_type = Fernet(key)
    dmongoUser = enc_type.decrypt(uname).decode("utf-8")
    
    pwd = bytes(secret.mongoPassword,'utf-8')
    keyp = bytes("oD73fNVIz5dK5MzkAz0LQ2wAGzw3fe3SNiGPjICES4E=","utf-8")
    p_enc_type = Fernet(keyp)
    dmongoPwd = p_enc_type.decrypt(pwd).decode("utf-8")
    
    try:
        mongoClient = pymongo.MongoClient("mongodb+srv://"+dmongoUser+":"+dmongoPwd+"@cluster0.cv48i.mongodb.net/NYTimes?retryWrites=true&w=majority")
    except ConnectionFailure:
        print("Failed to connect to database")
        return "Service Error: Unexpectd Error occured while processing your request HTTP 503 Service Unavailable"
    return mongoClient

# The following method is used to retrieve all the book review records from remote MongoDB collection.
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

# The following mthod is used to retrieve specific book review records from remote MongoDB collection.
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

# The following method is used to validate the parameters sent as request payload.
def checkParams(params):
    if (params==None or params['name']==None or params['author'] or params['review']==None or params['link']==None):
        print("Bad Request: The name of request parameters should be as per documentation")
        return "Bad Request: Request parameter name not found HTTP 400 Bad Request"

# The following method is used to submit a book review to the remote MongoDB collection.
def insertBookReview(collection,params):
    try:
        collection.insert_one(params)
        print("Data insertion successful")
        return "Success: Review Submitted Successfully!! HTTP 201 OK"
    except CollectionInvalid:
        print("Invalid Collection")
        return "Request Error: Could not query the collection. "

