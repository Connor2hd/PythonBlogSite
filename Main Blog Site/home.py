#Imports
import pymongo
import datetime
from pprint import pprint
from pymongo import MongoClient
from bottle import route, run, request, response, get, delete, post, hook, template
from pymongo.errors import PyMongoError
import re
from bson import ObjectId

#Set the address for Mongo client
client = MongoClient('localhost', 27017)

#set the database variable
db = client.lab3

#set the collections
blogcoll = db.Posts
usercoll = db.Users

#Login page
@route('/')
def login():
    return template('login')

#hanlde login requests
@route('/login', method="POST")
def login():
    try:
        try:
            username = request.forms.get("txtUsername")
            password = request.forms.get("txtPassword")
            login_doc = usercoll.find_one({"username":username, "password":password})
            if login_doc is None:
                raise ValueError
            #this is where the code was
        except PyMongoError:
            raise EnvironmentError
    except ValueError:
        response.status = 400
        return ({"error":"No User matching those credentials found"})
    except EnvironmentError:
        response.status = 500
        return ({"error":"User data is unavailable"})

    p_list = blogcoll.find({"author": username}).sort('date',pymongo.DESCENDING)
    return template('home', {"Posts": list(p_list)}, lblUsername=username)

#Page with all blogs
@route('/allBlogs')
def allBlogs():
    try:
        try:
            p_list = blogcoll.find({}).sort('date',pymongo.DESCENDING)
            if p_list is None:
                raise EnvironmentError
        except PyMongoError:
            raise EnvironmentError
    except EnvironmentError:
        response.status = 500
        return ({"error":"Blog post data is not available"})

    return template('allBlogs', {"Posts": list(p_list)})

#Delete a post
@route('/deletePost', method="POST")
def remove_post():
    try:
        #build reg ex
        id = request.forms.get("id")
        author = request.forms.get("author")
        pattern = r'^[a-fA-F0-9]{24}$'
        #check if the reg ez pattern matches the objectid passed to Method
        if re.search(pattern, id) is None:
            raise TypeError
        try:
            id = ObjectId(id)
            results = blogcoll.delete_one({"_id":id})
            #blogs not Found
            if results.deleted_count == 0:
                raise ValueError
        except PyMongoError:
            raise EnvironmentError

    except TypeError:
        response.status = 400
        return({"error": "Unacceptable ObjectID value"})
    except ValueError:
        response.status = 404
        return ({"error": "Blog post not found"})
    except EnvironmentError:
        response.status = 500
        return ({"error": "Blog data is not Available"})

    #return the user home
    p_list = blogcoll.find({"author": author}).sort('date',pymongo.DESCENDING)
    return template('home', {"Posts": list(p_list)}, lblUsername=author)


#Code to insert a new post
@route('/insertPost', method="POST")
def insert_post():
    author = request.forms.get("username")
    text = request.forms.get("blogText")

    #Create a post object
    post = {"author": author,
            "text": text,
            "date": datetime.datetime.utcnow(),
            "comments":[]}

    #insert post object into database
    blogcoll.insert(post)

    #return the user home
    p_list = blogcoll.find({"author": author}).sort('date',pymongo.DESCENDING)
    return template('home', {"Posts": list(p_list)}, lblUsername=author)

#Code to insert a new comment
@route('/insertComment', method="POST")
def insert_comment():
    author = request.forms.get("author")
    text = request.forms.get("commentText")
    postId = request.forms.get("postId")

    #Create a comment objectid
    comment = {"commentAuthor": author,
                "commentText": text,
                "commentDate": datetime.datetime.utcnow()}

    #push the item into the array
    id = ObjectId(postId)
    blogcoll.update({'_id':id}, { '$push': {'comments': comment}})

    #return the user home
    p_list = blogcoll.find({"author": author}).sort('date',pymongo.DESCENDING)
    return template('home', {"Posts": list(p_list)}, lblUsername=author)

#Code to get values to update page
@route('/updatePostPage', method="POST")
def update_postPage():
    postId = request.forms.get("id")

    #Get the document to be updated
    id = ObjectId(postId)
    p_list = blogcoll.find({'_id':id})

    return template('updatePost', {"Posts": list(p_list)})

#Code to handle update request
@route('/updatePost', method="POST")
def update_post():
    postId = request.forms.get("id")
    newText = request.forms.get("newText")
    author = request.forms.get("author")

    #update document
    id = ObjectId(postId)
    blogcoll.update({'_id':id}, {'$set': {"text": newText}}, upsert=True)

    #bring user back home
    p_list = blogcoll.find({"author": author}).sort('date',pymongo.DESCENDING)
    return template('home', {"Posts": list(p_list)}, lblUsername=author)


#run on localhost
run(host='localhost', port=8080)
