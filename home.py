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

#load the template
@route('/')
def index():
    p_list = collection.find({"author": "Alex"}).sort('date',pymongo.DESCENDING)
    return template('home', {"collection": list(p_list)})

#run on localhost
run(host='localhost', port=8080)
