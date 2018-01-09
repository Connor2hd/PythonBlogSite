from bottle import route, run, request, response, get, delete, post, hook
from bson.json_util import dumps
from bson import ObjectId
from pymongo.errors import PyMongoError
from pymongo import MongoClient
import re

#Establish connection
mongo_client = MongoClient("localhost", 27017)
db = mongo_client.lab3
coll = db.Posts

#Get all blog posts
@get('/blog_posts')
def get_posts():
    try:
        try:
            #Find posts and sort by insertion time
            p_list = coll.find({}).sort("date")
            #if the list is not found it is because the collection is empty or does not exist
            if p_list is None:
                raise EnvironmentError
        except PyMongoError:
            raise EnvironmentError
    except EnvironmentError:
        response.status = 500 #Internal server error
        return ({"error":"Blog Post Data is Not Available"})

    response.headers['Cache-Control'] = 'cache' #permit caching
    return dumps({"Blog": p_list})


#Get all blog posts for a single user
@get('/blog_posts/<author>')
def get_posts(author):
    try:
        try:
            #Retrieve blogs that match author passed in
            b_list = coll.find({"author":author})
            #test to see if posts exist for that user
            if b_list is None:
                raise ValueError
        except PyMongoError:
            raise EnvironmentError
    except ValueError:
        response.status = 400
        return ({"error":"No blog posts for that user found"})
    except EnvironmentError:
        response.status = 500
        return ({"error":"Blog data is not available"})

    response.headers['Cache-Control'] = 'cache'
    return dumps({"Posts":b_list})


#Add or update blog post (post)
@post('/blog_posts')
def set_blog():
    id = request.params.get('id')
    author = request.params.get('author')
    text = request.params.get('text')
    date = request.params.get('date')

    try:
        #build reg ex
        pattern = r'^[a-fA-F0-9]{24}$'
        #check is the regex pattern matches the objectib passed to the Method
        if re.search(pattern, id) is None:
            raise TypeError

        if (author is None) or (text is None) or (date is None):
            raise ValueError

        try:
            id = ObjectId(id)
            results = coll.update_one({"_id":id}, {"$set": {"author": author, "text": text, "date": date}}, upsert=True)
        except PyMongoError:
            raise EnvironmentError

    except TypeError:
        response.status = 400
        return ({"error": "Unacceptable ObjectID value"})
    except ValueError:
        reponse.status = 400
        return ({"error": "Incorrect parameter values in request - author, text, and date are required"})
    except EnvironmentError:
        response.status = 500
        return ({"error": "Blog data is not Available"})

    response.headers['Cache-Control'] = 'no-cache'
    return ({"num_mod": results.modified_count, "_id":str(results.upserted_id)})

#Delete a blog post
@delete('/blog_posts/<id>')
def remove_post(id):
    try:
        #build reg ex
        pattern = r'^[a-fA-F0-9]{24}$'
        #check if the reg ez pattern matches the objectid passed to Method
        if re.search(pattern, id) is None:
            raise TypeError
        try:
            id = ObjectId(id)
            results = coll.delete_one({"_id":id})
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

    response.headers['Cache-Control'] = 'no-cache'
    return ({"num_deleted": results.deleted_count})

@hook('after_request')
def enable_cors():
    response.headers['Content-Type']='application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods']='PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers']='Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

run(host = 'localhost', port = 8082, debug = True, reloader = True)
