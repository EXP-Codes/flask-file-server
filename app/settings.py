#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# -----------------------------------------------

import random
import string
from datetime import timedelta
import erb.yml as yaml
import os
PRJ_DIR = os.path.dirname(os.path.abspath(__file__))
CHARSET = 'utf-8'
SETTINGS_PATH = '%s/conf/settings.yml' % PRJ_DIR
FILES_STORAGE_DIR = '%s/files' % PRJ_DIR


class Settings :

    def __init__(self, settings_path, charset) -> None:
        if os.path.exists(settings_path) :
            with open(settings_path, 'r', encoding=charset) as file:
                context = yaml.load(file.read())

                app = context.get('APPLICATION')
                self.ENV = app.get('ENV')
                self.DEBUG = self._to_bool(app.get('DEBUG'))
                self.TESTING = self._to_bool(app.get('TESTING'))
                self.PREFERRED_URL_SCHEME = app.get('PREFERRED_URL_SCHEME')
                self.APPLICATION_ROOT = app.get('APPLICATION_ROOT')
                self.APPLICATION_NAME = app.get('APPLICATION_NAME')
                self.SERVER_NAME = app.get('SERVER_NAME')
                self.LOGIN_USERNAME = app.get('LOGIN_USERNAME')
                self.LOGIN_PASSWORD = app.get('LOGIN_PASSWORD')
                
                cookie = context.get('COOKIE')
                self.SECRET_KEY = cookie.get('SECRET_KEY') or self._gen_cookie_secret_key()
                self.PERMANENT_SESSION_LIFETIME = timedelta(int(cookie.get('PERMANENT_SESSION_LIFETIME')))
                self.SESSION_COOKIE_NAME = cookie.get('SESSION_COOKIE_NAME')
                self.SESSION_COOKIE_DOMAIN = cookie.get('SESSION_COOKIE_DOMAIN')
                self.SESSION_COOKIE_PATH = cookie.get('SESSION_COOKIE_PATH')
                self.SESSION_COOKIE_HTTPONLY = self._to_bool(cookie.get('SESSION_COOKIE_HTTPONLY'))
                self.SESSION_COOKIE_SECURE = self._to_bool(cookie.get('SESSION_COOKIE_SECURE'))
                self.SESSION_COOKIE_SAMESITE = cookie.get('SESSION_COOKIE_SAMESITE')
                self.SESSION_REFRESH_EACH_REQUEST = self._to_bool(cookie.get('SESSION_REFRESH_EACH_REQUEST'))
                self.MAX_COOKIE_SIZE = int(cookie.get('MAX_COOKIE_SIZE'))

                content = context.get('CONTENT')
                self.BASEDIR = content.get('BASEDIR') or FILES_STORAGE_DIR
                self.MAX_CONTENT_LENGTH = content.get('MAX_CONTENT_LENGTH')
                self.JSON_AS_ASCII = self._to_bool(content.get('JSON_AS_ASCII'))
                self.JSON_SORT_KEYS = self._to_bool(content.get('JSON_SORT_KEYS'))
                self.JSONIFY_PRETTYPRINT_REGULAR = self._to_bool(content.get('JSONIFY_PRETTYPRINT_REGULAR'))
                self.JSONIFY_MIMETYPE = content.get('JSONIFY_MIMETYPE')
                self.TEMPLATES_AUTO_RELOAD = content.get('TEMPLATES_AUTO_RELOAD')

                other = context.get('OTHER')
                self.PROPAGATE_EXCEPTIONS = other.get('PROPAGATE_EXCEPTIONS')
                self.PRESERVE_CONTEXT_ON_EXCEPTION = other.get('PRESERVE_CONTEXT_ON_EXCEPTION')
                self.USE_X_SENDFILE = self._to_bool(other.get('USE_X_SENDFILE'))
                self.SEND_FILE_MAX_AGE_DEFAULT = other.get('SEND_FILE_MAX_AGE_DEFAULT')
                self.TRAP_BAD_REQUEST_ERRORS = other.get('TRAP_BAD_REQUEST_ERRORS')
                self.TRAP_HTTP_EXCEPTIONS = self._to_bool(other.get('TRAP_HTTP_EXCEPTIONS'))
                self.EXPLAIN_TEMPLATE_LOADING = self._to_bool(other.get('EXPLAIN_TEMPLATE_LOADING'))


    def _gen_cookie_secret_key(self, size=32) :
        return ''.join(
            random.sample(string.ascii_letters + string.digits, size)
        )

    
    def _to_bool(self, val) :
        if val is not None and not isinstance(val, bool) :
            if val.lower() == 'false' :
                val = False
            elif val.lower() == 'true' :
                val = True
        return val



settings = Settings(SETTINGS_PATH, CHARSET)

