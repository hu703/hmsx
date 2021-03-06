from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import os

# 修改Flask类
class Application(Flask):
    def __init__(self,import_name,template_folder=None,root_path=None,static_folder=None):
        super(Application,self).__init__(import_name=import_name,template_folder=template_folder,root_path=root_path,static_folder=static_folder)
        self.config.from_pyfile("config/base_setting.py")  # 导入配置文件
        if 'ops_config' in os.environ:
            self.config.from_pyfile("config/%s_setting.py"%os.environ['ops_config'])
        db.init_app(self)   # 初始化数据库


# 实例化
db = SQLAlchemy()  # 初始化db  要在初始化数据库之前
app = Application(__name__,template_folder=os.getcwd()+"/web/templates/",root_path=os.getcwd(),static_folder=os.getcwd()+'/web/static')
# app是应用 manager管理命令
manager = Manager(app)




# 函数模板
from common.libs.UrlManager import UrlManager
app.add_template_global(UrlManager.buildUrl,'buildUrl')
app.add_template_global(UrlManager.buildStaticUrl,'buildStaticUrl')
app.add_template_global(UrlManager.buildImageUrl,'buildImageUrl')
