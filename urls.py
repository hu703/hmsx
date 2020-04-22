from application import app
# 注册
from web.controllers.user.User import rooter_user

app.register_blueprint(rooter_user,url_prefix='/user')