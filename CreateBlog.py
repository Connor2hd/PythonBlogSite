#Imports
import pymongo
import datetime
from pprint import pprint
from pymongo import MongoClient
from bottle import route
from bottle import run
from bottle import template

#Set the address for Mongo client
client = MongoClient('localhost', 27017)

#set the database variable
db = client.lab3

#set the collection
collection = db.collection

# Create sample posts
posts = [{"author": "Alex",
        "text": "Blog post 1",
        "date": datetime.datetime.utcnow(),
        "comments": [
            {"commentAuthor": "Adam",
            "commentText": "Blog 1 Comment 1",
            "commentDate": datetime.datetime.utcnow()},
            {"commentAuthor": "Bob",
            "commentText": "Blog 1 Comment 2",
            "commentDate": datetime.datetime.utcnow()},
            {"commentAuthor": "Charlie",
            "commentText": "Blog 1 Comment 3",
            "commentDate": datetime.datetime.utcnow()},
        ]},
        {"author": "Bill",
        "text": "Blog post 2",
        "date": datetime.datetime.utcnow(),
        "comments": [
            {"commentAuthor": "Andrew",
            "commentText": "Blog 2 Comment 1",
            "commentDate": datetime.datetime.utcnow()},
            {"commentAuthor": "Bishop",
            "commentText": "Blog 2 Comment 2",
            "commentDate": datetime.datetime.utcnow()},
            {"commentAuthor": "Connor",
            "commentText": "Blog 3 Comment 3",
            "commentDate": datetime.datetime.utcnow()},
        ]}]

#insert sample Posts
db.collection.insert(posts)

#load the template
@route('/')
def index():
    p_list = collection.find({"author": "Alex"})
    return template('home', {"collection": list(p_list)})

#run on localhost
run(host='localhost', port=8080)
