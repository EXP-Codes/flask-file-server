#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------

from flask import Flask, render_template, session, request, redirect, url_for
from .views.account import account
from .views.home import home
from .app_conf import AppConfig


def create_webapp():
    
    app = Flask(__name__)
    app.register_blueprint(account, url_prefix='/')
    app.register_blueprint(home)
    app.config.from_object(AppConfig)

    @app.before_request
    def check() :
        if not session.get('user') and \
            not request.path.startswith('/static') \
            and request.path != '/login':
            return redirect(url_for('account.login'))


    @app.template_filter("split_path")
    def split_path(path) :
        path_list = path.split('/')
        path_list = [[path_list[i - 1], '/'.join(path_list[:i])] for i in range(1, len(path_list)+1)]
        return path_list


    @app.errorhandler(404)
    def error(error_no):
        return render_template('error_404.html')

    return app
