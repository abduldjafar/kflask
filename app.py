from router import *
from flask import Flask
from models import *
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.register_blueprint(routes)

app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
#app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)


generateUser()


if __name__ == "__main__":
    app.run()