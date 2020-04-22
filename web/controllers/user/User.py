from flask import Blueprint

rooter_user = Blueprint('user_page',__name__)
@rooter_user.route("/login")
def login():
    return "login 页面"