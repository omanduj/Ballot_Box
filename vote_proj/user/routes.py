from flask import Flask, jsonify, request, render_template
from flask_file import app
from user.models import User, get_ballots, get_items_voter, vote, del_img
from flask_socketio import SocketIO, emit
from bson import json_util

import json
socketio = SocketIO(app)

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

@socketio.on('voting')
@app.route('/destroyImage', methods=["POST"])
def delete_img():
    item_name = request.form.get('item_name')
    ballot_name = request.form.get('ballot_name')
    del_img(item_name, ballot_name)
    ballot_item_dict = get_ballots()
    socketio.emit('left_over', {'results1': ballot_item_dict[ballot_name]}, broadcast=True)
    return ({"Close": "X"})

@app.route('/user/add_ballot_item', methods=["POST"])             #being used in scripts.js file
def add_ballot_item():
    item_name = request.form.get('item_name')
    image = request.form.get('image')
    description = request.form.get('description')
    return User().add_ballot_item(item_name, image, description)

@socketio.on('remove')
@app.route('/dashboard/<ballot_name>', methods=["GET"])
def profile(ballot_name):
    item = get_items_voter(ballot_name)
    return render_template('voter_page.html', item=item, ballot_name=ballot_name)

@app.route('/voting', methods=["POST"])
def voting():
    item_name = request.form.get('name')
    ballot_name = request.form.get('ballot_name')
    amount_of_votes = vote(item_name, ballot_name)
    socketio.emit('vote_results', {'results1': amount_of_votes, 'item_name': item_name}, broadcast=True)
    return {'success': "Complete"}, 200

def get_ballot_items():
    ballot_item_dict = get_ballots()
    ballot_names = ballot_item_dict.keys()
    ballot_names = list(ballot_names)
    return ballot_item_dict, ballot_names
