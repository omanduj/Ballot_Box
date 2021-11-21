from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256          #used to hash password
from flask_file import db

import uuid     #used to make _id easier to use?

class User():

    def start_session(self, user):          #used in the login in class method
        del user['password']
        session['logged_in'] = True
        session['user'] = user

        return jsonify(user), 200

    def signup(self):                           #used in routes signup endpoint
        #Create user object
        user = {
            '_id': uuid.uuid4().hex,
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'password': request.form.get('password')
        }

        #encrypt password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        if db.users.find_one({'email': user['email']}):
            return jsonify({'error': 'Email already in use'}), 400

        if db.users.insert_one(user):     #in the predefined db, in the users collection, insert user object
            return self.start_session(user)     #to have this execute import session from flask and define session secret key in flask_file.py

        return jsonify({'error': 'Sign Up failed'}), 400

    def signout(self):                              #used in html as endpoint on logout page
        session.clear()
        return redirect('/')


    def login(self):                                   #used in routes as login endpoint
        user = db.users.find_one(
            {'email': request.form.get('email')}
        )

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)

        return jsonify({ 'error': 'Invalid Credentials' }), 401

    def add_ballot_name(self,item):
        session['ballot_items'] = item
        db.users.update({"email": session['user']['email']},
                     {"$set": {"ballot_items.{}".format(item): {} } } );
        return jsonify({'success': 'Ballot added'}), 200

    def add_ballot_item(self, item_name, image, description):
        db.users.update({"email": session['user']['email']},
                        {"$set": {"ballot_items.{}.{}".format(session['ballot_items'], item_name): {'image': image, 'description': description, 'votes': 0} } } );
        return jsonify({'success': 'Item added'}), 200

def get_ballots():
    new_dict = {}
    ballots = db.users.find({ 'email': session['user']['email'] })
    ballots = list(ballots)

    for item in ballots:
       name = item['name']
       new_dict[name] = item

    my_keys = list(new_dict[session['user']['name']].keys())

    if 'ballot_items' in my_keys:
        ballot_item_dict = new_dict[session['user']['name']]['ballot_items']
        return ballot_item_dict
    return {"No Ballots": "Make Some Ballots!"}
