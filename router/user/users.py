from flask import render_template,request
from router import routes
from controller.userController import users,profiles
from models import *

user = users.user()
profile = profiles.profile()

@routes.route('/profile',methods=['POST','GET','PUT'])
def users():
    if request.method == 'POST' :
        return profile.addProfile()
    elif request.method == 'PUT':
        return profile.updateProfile()
    else:
        return profile.getProfile()

@routes.route('/login', methods=['POST'])
def login():
    return user.login()

@routes.route('/register', methods=['POST'])
def register():
    return user.addUser()