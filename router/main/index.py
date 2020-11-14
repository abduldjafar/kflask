from router import routes

@routes.route('/')
def index():
    return "index"