from flask import Flask, render_template, session, redirect, request
from functools import wraps
from flask_avatars import Avatars
import pymongo
import requests
import hashlib  # used for avatars

app = Flask(__name__)
app.secret_key = b"\x19\xad\xa4?\xb72\xca.H\ng=\xa4\xcdW\xc2"  # needed to run sessions
avatars = Avatars(
    app
)  # Used to obtain personal Avatars for users based on their emails
client = pymongo.MongoClient("mongodb://localhost:27017/")  # connect to db
db = (
    client.user_login_system
)  # this creates database with the name user_login_system, and associated it with variable db

# decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            return redirect("/")

    return wrap


# to see mongodb, go to shell run mongosh, then run "show dbs" then "use <dbs name>" then
# "show collections" then "db.collectionName.find()"

# imports route names from seperate file
from user import routes
from user.routes import get_ballot_items
from user.models import get_email


@app.route("/")
def home():
    """Purpose: To function as login page for application
    Parameters: N/a
    Return Value: html page that provides login and signup functionality
    """
    return render_template("home.html")


@app.route("/dashboard/")
@login_required
def dashboard():
    """Purpose: To serve as dashboard displaying user information and previouly made ballots and their vote count
    Parameters: N/a
    Return Value: html page the displays user information and previouly made ballots and their vote count
    """
    ballot_item_dict, ballot_names = get_ballot_items()
    email = get_email()
    avatar_hash = hashlib.md5(email.lower().encode("utf-8")).hexdigest()
    return render_template(
        "dashboard.html",
        ballot_item_dict=ballot_item_dict,
        ballot_names=ballot_names,
        avatar_hash=avatar_hash,
    )


@app.route("/ballot_name/")
@login_required
def ballot_name():
    """Purpose: To provide the name of a ballot that will be added to users account
    Parameters: N/a
    Return Value: html that allows user to name next ballot that they wish to use
    """
    return render_template("ballot_name.html")


@app.route("/ballot_items/")
@login_required
def add_items():
    """Purpose: Allows users to define what items should be included in the ballot
    Parameters: N/a
    Return Value: html page used to store user input on a ballot item such as description, image and item name
    """
    return render_template("ballot_items.html")
