#Install Pymongo
import pymongo

#install pprint, makes output easier to read
from pprint import pprint

#Create a mongod instance
from pymongo import MongoClient
client = MongoClient()

#Set the address for Mongo client
client = MongoClient('localhost', 27017)

#set the database variable
db = client.lab3

# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
