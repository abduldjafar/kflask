from pony.orm import *
from passlib.hash import pbkdf2_sha256 as sha256
import time, datetime


db = Database("mysql", host="localhost", user="root", passwd="toor", db="kotekaman")


class User(db.Entity):
    email=PrimaryKey(str)
    password=Required(str)
    profile=set('Profile')

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

class Profile(db.Entity):
    email_user = Required(str,unique=True)
    company_name = Required(str)
    street_number = Required(str)
    street_name = Required(str)
    zip = Required(str)
    city = Required(str)
    office_phone = Required(str)
    mobile_phone = Required(str)
    company_reg_numb = Required(str)
    subc = Required(str)
    approval = Required(str)


class TokenBlacklist(db.Entity):
    id = PrimaryKey(int,auto=True)
    jti = Required(str)
    token_type = Required(str)
    user_identity = Required(str)
    revoked = Required(bool)
    expires =Required(datetime.datetime)

def generateUser():
    db.generate_mapping(create_tables=True)


    # there is no need to call commit() here -
    # Pony does it automatically on leaving the db_session scope


