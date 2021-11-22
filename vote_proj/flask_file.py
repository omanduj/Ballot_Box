from flask import Flask, render_template, session, redirect
from functools import wraps
import pymongo

app = Flask(__name__)
app.secret_key = b'\x19\xad\xa4?\xb72\xca.H\ng=\xa4\xcdW\xc2' #needed to run sessions

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

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/dashboard/')
@login_required
def dashboard():
    ballot_item_dict, ballot_names = get_ballot_items()
    return render_template('dashboard.html', ballot_item_dict=ballot_item_dict, ballot_names=ballot_names)

@app.route('/ballot_name/')
@login_required
def ballot_name():
    return render_template('ballot_name.html')

@app.route('/ballot_items/')
@login_required
def add_items():
    return render_template('ballot_items.html')
