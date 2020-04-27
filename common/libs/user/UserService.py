import hashlib,base64

class UserService():
    # 生成密码结合pwd，salt
    @staticmethod
    def generatePwd(pwd,salt):
        m = hashlib.md5()
        str = "%s-%s"%(base64.encodebytes(pwd.encode('utf-8')),salt)  # 将pwd和salt结合 pwd改为utf-8的二进制
        m.update(str.encode("utf-8")) # 变为一个加密的字符串
        return m.hexdigest() # 返回一个新的密码

    # 生成cookie的加密值
    @staticmethod
    def generateAuthCode(user_info=None):
        m = hashlib.md5()
        str = "%s-%s-%s-%s"%(user_info.uid,user_info.login_name,user_info.pwd,user_info.login_salt)
        m.update(str.encode("utf-8"))
        return m.hexdigest()
