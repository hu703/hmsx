from flask import Blueprint,render_template,request,jsonify

rooter_user = Blueprint('user_page',__name__)
@rooter_user.route("/login",methods=['get','post'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')
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

    return jsonify(resp)

@rooter_user.route('/logout')
def logout():
    return "logout 页面"


@rooter_user.route('/edit')
def edit():
    return "edit 页面"


@rooter_user.route('/reset_pwd')
def reset_pwd():
    return "重置密码页面"