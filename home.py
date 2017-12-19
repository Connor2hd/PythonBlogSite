#Imports
import pymongo
import datetime
from pprint import pprint
from pymongo import MongoClient
from bottle import route
from bottle import run
from bottle import template
from bottle import request

#Set the address for Mongo client
client = MongoClient('localhost', 27017)

#set the database variable
db = client.lab3

#set the collection
collection = db.collection

#Homepage template with users blog posts
@route('/')
def index():
    p_list = collection.find({"author": "Alex"}).sort('date',pymongo.DESCENDING)
    return template('home', {"collection": list(p_list)})

@route('/createPost')
def create_post():
    author = "Alex"
    return template('createPost')

#Create Post page
@route('/insertPost', method="POST")
def insert_post():
    author = "Alex"
    text = request.forms.get("blogText")

    #Create a post object
    post = {"author": author,
            "text": text,
            "date": datetime.datetime.utcnow(),
            "comments":""}

    #insert post object into database
    db.collection.insert(post)

#@route('/createPost', method="POST")
#    author = "Alex"
#    text = request.forms.get('text')

#run on localhost
run(host='localhost', port=8080)
