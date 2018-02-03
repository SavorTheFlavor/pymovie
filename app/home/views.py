from . import home  # import home blueprint


@home.route("/")
def index():
    return "<h1 style='color: green;'>this is home!</h1>"

