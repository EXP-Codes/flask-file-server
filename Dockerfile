FROM ubuntu:18.04

# 设置系统文字字符集环境（因上传文件名可能含中文，故必须）
ENV PYTHONIOENCODING=UTF-8
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV LANGUAGE=C.UTF-8

RUN apt-get clean && \
    apt-get update -y && \
    apt-get install -y locales language-pack-zh-hans vim nginx python3 python3-pip
RUN ln -s /usr/bin/python3 /usr/bin/python && \
    python -m pip install --upgrade pip

# 安装系统中文语言包（因上传文件名可能含中文，故必须）
RUN locale-gen zh_CN.UTF-8

# 安装项目依赖
COPY ./app/requirements.txt /app/requirements.txt
RUN python -m pip install -r /app/requirements.txt

# 拷贝项目文件
COPY ./app /app
COPY ./nginx/flask.conf /etc/nginx/conf.d/flask.conf


EXPOSE 8080
WORKDIR /app
ENTRYPOINT [ "./entrypoint.sh" ]
# CMD [ "/usr/bin/python", "main.py" ]
