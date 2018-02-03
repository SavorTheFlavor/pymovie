from . import admin  # import admin blueprint


@admin.route("/")
def index():
    return "<h1 style='color:red;'>this is admin!</h1>"
