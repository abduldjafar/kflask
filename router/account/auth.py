from router import routes
from controller.accountController import auth

authss = auth.auth()

@routes.route('/auth')
def auths():
    return authss.auth()