# 设置服务器端口,在manage.py中的port引用
SERVER_PORT = 5000

# 链接数据库
SQLALCHEMY_DATABASE_URI = 'mysql://huhu:root@127.0.0.1/hmsx_db?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False


# 自动登录的cookie
AUTH_COOKIE_NAME = '1903'


# 拦截器忽略规则,与authInterceptors里的相对应
IGNORE_URLS = ['^/user/login']
IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]