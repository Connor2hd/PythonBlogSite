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
        "text": "The beaver (genus Castor) is a large, primarily nocturnal, semiaquatic rodent. Castor includes two extant species, the North American beaver (Castor canadensis) (native to North America) and Eurasian beaver (Castor fiber) (Eurasia).[1] Beavers are known for building dams, canals, and lodges (homes). They are the second-largest rodent in the world (after the capybara). Their colonies create one or more dams to provide still, deep water to protect against predators, and to float food and building material. The North American beaver population was once more than 60 million, but as of 1988 was 6–12 million. This population decline is the result of extensive hunting for fur, for glands used as medicine and perfume, and because the beavers' harvesting of trees and flooding of waterways may interfere with other land uses.[2]",
        "date": datetime.datetime.utcnow(),
        "comments": [
            {"commentAuthor": "Adam",
            "commentText": "Blog 1 Comment ",
            "commentDate": datetime.datetime.utcnow()},
            {"commentAuthor": "Bob",
            "commentText": "Blog 1 Comment 2",
            "commentDate": datetime.datetime.utcnow()},
            {"commentAuthor": "Charlie",
            "commentText": "Blog 1 Comment 3",
            "commentDate": datetime.datetime.utcnow()},
        ]},
        {"author": "Bill",
        "text": "The mallard is considered to be a species of least concern by the International Union for Conservation of Nature (IUCN). Unlike many waterfowl, mallards are considered an invasive species in some regions. It is a very adaptable species, being able to live and even thrive in urban areas which may have supported more localised, sensitive species of waterfowl before development. The non-migratory mallard interbreeds with indigenous wild ducks of closely related species through genetic pollution by producing fertile offspring. Complete hybridisation of various species of wild duck gene pools could result in the extinction of many indigenous waterfowl. The wild mallard is the ancestor of most domestic ducks, and its naturally evolved wild gene pool gets genetically polluted by the domesticated and feral mallard populations.",
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
