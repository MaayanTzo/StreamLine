from bottle import *
import feedparser
import json


@route('/')
def index():
    return static_file("LP.html", root='')

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='')

@route('/<filename:re:.*\.js>')
def stylesheets(filename):
    return static_file(filename, root='')

@post('/get-playlist')
def get_articles():
    articles="hello"
    return json.dumps(articles)

if __name__ == '__main__':
    run(host='localhost',port=7000, debug=True)