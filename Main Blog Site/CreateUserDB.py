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
collection = db.Users

# Create sample users
posts = [{"username": "Alex",
        "password": "Password1",
        },
        {"author": "Bill",
        "text": "Password2",
        }]

#insert sample Posts
db.Users.insert(posts)
