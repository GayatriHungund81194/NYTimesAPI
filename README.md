# NYTimesAPI for Book Review

The repository contains the code for the API that allows user to view and submit book reviews. The is deployed on Heroku and can be accessed from the following URL:
https://sheltered-caverns-61168.herokuapp.com/

Following is the link to API documentation that includes sample requests and responses for better understanding:
https://documenter.getpostman.com/view/8870976/TVCjy6QF

### API Endpoints
1. /getBooks - API endpoint to view book reviews.
2. /addReview - API endpoint to submit a book review.

### Technology Stack used to create the application:
1. Python - The coding laguage used to develop the backend is Python and the entire application is developed in virtual environment. All the dependencies are listed             in the file "requirements.txt" thus making it easy for the user to run the application in virtual environment easily without being worried about the                 dependencies. The API also involves the usage of Cryptography for secure resource access internally.

2. Flask - The REST API methods (GET and POST) to retrieve book reviews and submit book review respectively are programmed using Flask. Request parser and other important utilities play an important role in development of this API.

3. MongoDB - As per the requirement of storing the user data on server side, a cloud MongoDB cluster is deployed using MongoDB Atlas to ensure high stability and availability of the API. Cloud cluster decreses the chances of downtime reduces the chances of data loss instead of storing data on a local machine. 

3. Heroku - Inorder to access the API from anywhere, it is entirely deployed on Heroku with Github synchronization. The default home page displays a link to API documentation.

4. Postman - It is very important to run and test the API developed, hence, postman is used to generate documentation and test the API. Following are the screenshots of testing the API using Postman:

![github-small](https://github.com/GayatriHungund81194/pics/blob/master/APITest.png)

### Steps to execute the code on local environment
Excute the following commands inorder to execute the code on a local environment:
1. git clone https://github.com/GayatriHungund81194/NYTimesAPI.git
2. Navigate to NYTimesAPI directory and execute the command: source bin/activate
3. Now, to install all the requirements, execute the command: pip install -r requirements.txt
4. To run the flask application, execute the command: python3 app.py
5. Navigate to http://localhost:5000 to access the API. 
6. Follow the API documentation for better explanation of each request and response. The link to the documentation is mentioned above in this Readme file.
