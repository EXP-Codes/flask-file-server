#!/bin/sh

# nginx -c /etc/nginx/nginx.conf &
service nginx start

sleep 2

# uwsgi --http :9527 -s ./uwsgi.sock --chmod-socket=777 --manage-script-name --mount /uwsgi=main:APP
uwsgi --ini uwsgi.ini
