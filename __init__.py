from bottle import *

import json
from pymongo import MongoClient

client = MongoClient()
db = client.StreamLine

users = db.users

@route('/')
def index():
    return static_file("LP.html", root='')

@route('/')
def index():
    return static_file("index.html", root='')

@route('/images/<filename:re:.*\.(png|jpg|svg|jpeg)>')
def stylesheets(filename):
    return static_file(filename, root='images')

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='')

@route('/<filename:re:.*\.js>')
def stylesheets(filename):
    return static_file(filename, root='')

@get('/get-playlist')
def get_playlists():
    articles="hi"
    #playlist=users.findOne({'gender': , 'age': , 'destination': , 'duration': })
    return json.dumps(articles)

@post('/get-playlist')
def get_playlists():
    new_user = {
        "gender": request.forms.get("gender"),
        "age": request.forms.get("age"),
        "destination": request.forms.get("destination"),
        "duration": request.forms.get("duration")
    }
    return json.dumps(new_user)

if __name__ == '__main__':
    run(host='localhost',port=7050, debug=True)