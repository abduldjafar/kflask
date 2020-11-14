from flask import Blueprint
routes = Blueprint('router', __name__)

from router.main.index import *
from router.user.users import *
from .account import auth