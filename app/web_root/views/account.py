#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------

from flask import Blueprint, render_template, request, session, redirect, url_for, jsonify
from settings import settings

account = Blueprint('account', __name__)


@account.route("/")
@account.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('account.html', app_name=settings.APPLICATION_NAME)
    else:
        username = request.form.get('user')
        password = request.form.get('pwd')
        if username == settings.LOGIN_USERNAME and \
            password == settings.LOGIN_PASSWORD :
            session['user'] = username
            return jsonify({"code": 200, "error": ""})
        else:
            return jsonify({"code": 401, "error": "用户名或密码错误"})


@account.route('/logout')
def logout():
    del session['user']
    return redirect(url_for('account.login'))
