from application import app,manager
from flask_script import Server
import urls


# web 服务器的配置

# use_debugger debug模式是否开启   use_reloader  热加载模式
manager.add_command("runserver",Server(host="localhost",port=app.config['SERVER_PORT'],use_debugger=True,use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()