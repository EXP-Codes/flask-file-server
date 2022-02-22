#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# 直接运行（不能搭配 nginx，仅本地可访问）： 
#   python main.py
# -----------------------------------------------
# 通过 uWSGI 运行（可搭配 nginx）：
#   uwsgi --http :9527 -s /{FULLPATH}/flask-file-server/app/{ANYNAME}.sock --manage-script-name --mount /{ANYNAME}=main:APP
#
# uWSGI 指引：https://dormousehole.readthedocs.io/en/latest/deploying/uwsgi.html
# -----------------------------------------------


from web_root.app import create_webapp
APP = create_webapp()


# 官方原文： 
# 请务必把 app.run() 放在 if __name__ == '__main__': 内部或者放在单独 的文件中，这样可以保证它不会被调用。
# 因为，每调用一次就会开启一个本地 WSGI 服务器。当我们使用 uWSGI 部署应用时，不需要使用本地服务器。
if __name__ == '__main__':
    APP.run()


