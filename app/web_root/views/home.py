#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------

from settings import settings
from flask import Blueprint, render_template, current_app, send_from_directory, request, jsonify
from werkzeug.utils import secure_filename
import os
import time

home = Blueprint('home', __name__)


class DocumentReader:

    def __init__(self, real_path):
        self.real_path = real_path


    def analysis_dir(self):
        dirs = []
        files = []
        os.chdir(self.real_path)
        for name in sorted(os.listdir('.'), key=lambda x: x.lower()):
            _time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime(name)))
            if os.path.isdir(name):
                dirs.append([name, _time, '文件夹', '-'])
            elif os.path.isfile(name):
                file_type = os.path.splitext(name)[1]
                size = self.get_size(os.path.getsize(name))
                files.append([name, _time, file_type, size])
        return dirs, files


    @staticmethod
    def get_size(size):
        if size < 1024:
            return '%d  B' % size
        elif 1024 <= size < 1024 * 1024:
            return '%.2f KB' % (size / 1024)
        elif 1024 * 1024 <= size < 1024 * 1024 * 1024:
            return '%.2f MB' % (size / (1024 * 1024))
        else:
            return '%.2f GB' % (size / (1024 * 1024 * 1024))



@home.route('/index')
@home.route('/index/<path:path_uri>')
def index(path_uri=''):
    base_dir = settings.BASEDIR
    real_path = os.path.join(base_dir, path_uri).replace('\\', '/')

    if not os.path.exists(real_path):
        html = render_template('error_404.html')
    else :
        file_reader = DocumentReader(real_path)
        dirs, files = file_reader.analysis_dir()
        html = render_template('index.html', 
            app_name=settings.APPLICATION_NAME, 
            path=path_uri, 
            dirs=dirs, 
            files=files, 
            error_info=None
        )
    return html


@home.route('/download/<filename>')
@home.route('/download/<path:path>/<filename>')
def download(filename, path=None):
    if not path:
        real_path = settings.BASEDIR
    else:
        real_path = os.path.join(settings.BASEDIR, path)
    return send_from_directory(real_path, filename, mimetype='application/octet-stream')


@home.route('/upload', methods=['GET', 'POST'])
def upload():
    html = ''
    if request.method == 'POST' :
        path = request.form.get('upload_path')
        file = request.files['upload_file']
        base_dir = settings.BASEDIR

        if file :
            filename = _get_filename(file)
            save_path = os.path.join(base_dir, path, filename)
            file.save(save_path)
            html = jsonify({"code": 200, "info": "文件：%s 上传成功" % filename})
        else :
            html = jsonify({"code": 201, "info": "未选择文件"})
    else :
        html = jsonify({"code": 201, "info": "禁止使用爬虫上传文件"})
    return html


def _get_filename(file) :
    return file.filename
    # secure_filename 可以处理路径穿越等问题，但是会把文件名中中文去掉，故无法使用
    # return secure_filename(file.filename)


@home.errorhandler(500)
def error(error):
    return render_template('error_500.html')

