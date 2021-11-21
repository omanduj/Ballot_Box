from flask import Flask, jsonify, request
from flask_file import app
from user.models import User

#this endpoint is used to obtain data from the scripts.js file
#specifically from ("form[name=signup_form]") where "form" defines the html tag,
#"name" defines the tag attribute and "signup_form" defines what form should be used
#So in our case, the tag form whose name value is signup_form is used. Then using the ajax
#we define more info such as method, url (found here) etc

#from user.models import User allows access to User class, where we take the info posted to the URL
#below and create a user object with the info and run the class function signup, this adds the info to
#mongodb
@app.route('/user/signup', methods=["POST"])            #being used in scripts.js file
def signup():
    return User().signup()

@app.route('/user/signout', methods=["GET"])            #being used in dashboard.html file as href in form
def signout():
    return User().signout()

@app.route('/user/login', methods=["POST"])             #being used in scripts.js file
def login():
    return User().login()

@app.route('/user/add_ballot', methods=["POST"])             #being used in scripts.js file
def add_ballot():
    ballot_name = request.form.get('item_name')
    return User().add_ballot_name(ballot_name)
