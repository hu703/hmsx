from flask import Blueprint,render_template,request,jsonify,make_response,redirect

from common.models.User import User   # 引入user类
from common.libs.user.UserService import UserService  # 引入生成密码算法的类
import json
from common.libs.UrlManager import UrlManager
from common.libs.Helper import *
from application import app

rooter_user = Blueprint('user_page',__name__)
@rooter_user.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if g.current_user:
            return redirect(U)
        return ops_render('user/login.html')
    resp = {
        'code':200,
        'msg':'登录成功！',
        'data':{}
    }
    req = request.values
    login_name = req['login_name']
    login_pwd = req['login_pwd']
    # 后端校检 不为空 长度不小于1
    if login_name is None or len(login_name) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的用户名！'
        return jsonify(resp)
    if login_pwd is None or len(login_pwd) < 1:
        resp['code'] = -1
        resp['msg'] = '请输入正确的密码'
        return jsonify(resp)
    user_info = User.query.filter_by(login_name=login_name).first()
    print(user_info)
    if not user_info:
        resp['code'] = -1
        resp['msg'] = '用户名不存在'
        return jsonify(resp)
    if user_info.status != 1:
        resp['code'] = -1
        resp['msg'] = '账户已被禁用'
        return jsonify(resp)
    if user_info.login_pwd != UserService.generatePwd(login_pwd,user_info.login_salt):
        resp['code'] = -1
        resp['msg'] = '密码错误'
        return jsonify(resp)

    # 将用户信息存入到浏览器的cookie中
    # json.dumps() 只能处理dict list类型，经过处理可以直接在浏览器使用
    response = make_response(json.dumps({'code':200,'msg':'登录成功！'})) 
    # name value  过期时间
    # value包括login_name login_pwd  login_salt uid
    response.set_cookie(app.config["AUTH_COOKIE_NAME"],'%s@%s'%(UserService.generateAuthCode(user_info),user_info.uid),60*60*24*5)

    return response

@rooter_user.route("/edit",methods=['GET','POST'])
def edit():
    return render_template("/user/edit.html")

@rooter_user.route("/reset_pwd",methods=['GET','POST'])
def reset_pwd():
    return render_template("/user/reset_pwd.html")


@rooter_user.route("/logout",methods=['GET','POST'])
def logout():


