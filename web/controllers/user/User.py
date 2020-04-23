from flask import Blueprint,render_template

rooter_user = Blueprint('user_page',__name__)
@rooter_user.route("/login")
def login():
    return render_template('user/login.html')

@rooter_user.route('/logout')
def logout():
    return "logout 页面"


@rooter_user.route('/edit')
def edit():
    return "edit 页面"


@rooter_user.route('/reset_pwd')
def reset_pwd():
    return "重置密码页面"