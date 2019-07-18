from bottle import *

import json
from pymongo import MongoClient
from random import *
from playsound import playsound
import random

# from pymongo import MongoClient
#
# client = MongoClient('mongodb+srv://jonahmil:jonahmil@cluster0-q78ti.mongodb.net/test?retryWrites=true&w=majority')
# db = client.StreamLine
# >>>>>>> 643afd8921946007575a27b80e76b742cd5a1dc8

# users = db.users
# print(users)

@route('/')
def LP():
    return static_file("index.html", root='')

@route('/LP')
def index():
    return static_file("index.html", root='')


@route('/images/<filename:re:.*\.(png|jpg|svg|jpeg)>')
def imges(filename):
    return static_file(filename, root='images')


@route('/<filename:re:.*\.css>')
def css(filename):
    return static_file(filename, root='')

@route('/<filename:re:.*\.js>')
def js(filename):
    return static_file(filename, root='')

@get('/get-playlist')
def get_playlists():
    articles="hi"
    id=random.randint(1,6)
    playsound('C:\\Users\\Mikael\\Desktop\\ITC\\Hackathon\\StreamLine\\data\\' + str(id) + '.mp3')
    return json.dumps(articles)

@post('/get-playlist')
def get_playlists():
    new_user = request.POST.dict

    return json.dumps(new_user)

if __name__ == '__main__':
    run(host='localhost',port=7050, debug=True)