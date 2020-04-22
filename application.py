from flask import Flask
from flask_script import Manager
import os

# 修改Flask类
class Application(Flask):
    def __init__(self,import_name,template_folder=None,root_path=None):
        super(Application,self).__init__(import_name=import_name,template_folder=template_folder,root_path=root_path)

# 实例化
app = Application(__name__,template_folder=os.getcwd()+"/web/templates/",root_path=os.getcwd())
# app是应用 manager管理命令
manager = Manager(app)
