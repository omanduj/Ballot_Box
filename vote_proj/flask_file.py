from flask import Flask, render_template, session, redirect, request
from functools import wraps
from flask_avatars import Avatars
import pymongo
import requests
import hashlib

app = Flask(__name__)
app.secret_key = '' #needed to run sessions
avatars = Avatars(app)
#connect to db
client = pymongo.MongoClient('mongodb://localhost:27017/')
#this creates database with the name user_login_system, and associated it with variable db
db = client.user_login_system

#decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

#to see mongodb, go to shell run mongosh, then run "show dbs" then "use <dbs name>" then
# "show collections" then "db.collectionName.find()"

#imports route names from seperate file
from user import routes
from user.routes import get_ballot_items
from user.models import get_email

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
@login_required
def dashboard():
    ballot_item_dict, ballot_names = get_ballot_items()
    email = get_email()
    avatar_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
    return render_template('dashboard.html', ballot_item_dict=ballot_item_dict, ballot_names=ballot_names, avatar_hash=avatar_hash)

@app.route('/ballot_name/')
@login_required
def ballot_name():
    return render_template('ballot_name.html')

@app.route('/ballot_items/')
@login_required
def add_items():
    return render_template('ballot_items.html')
