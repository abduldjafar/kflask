from flask import request
from pony.orm.serialization import to_dict
import datetime
from flask_jwt_extended import (create_access_token, get_raw_jwt)


from models import *

class user(object):
    @db_session
    def login(self):
        email = request.form['email']
        password = request.form['password']
        try:
            user = User.get(email=email)
            print(user.verify_hash(password,user.password))
            if user.verify_hash(password,user.password):
                expires = datetime.timedelta(days=1)
                access_token = create_access_token(identity=email,expires_delta=expires)

                return {
                    'message': 'Logged in as {}'.format(email),
                    'access_token': access_token
                }
            else:
                return {'message': 'Wrong credentials'}
        except:
            return {'message': 'Something went wrong'}, 500

    @db_session
    def addUser(self):
        email = request.form['email']
        password = request.form['password']
        try:
            user = User(email=email,password=User.generate_hash(password))
            expires = datetime.timedelta(days=1)
            access_token = create_access_token(identity=email,expires_delta=expires)
            return {
                'message': 'User {} was created'.format(email),
                'access_token': access_token
            }
        except:
            return {'message': 'Something went wrong'}, 500

    def updateUser(self):
        pass

    def deleteUser(self):
        pass

    def logout(self):
        pass