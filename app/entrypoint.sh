#!/bin/sh

nginx -c /etc/nginx/nginx.conf &

sleep 2

# uwsgi --http :9527 -s ./uwsgi.sock --manage-script-name --mount /uwsgi=main:APP
uwsgi --ini uwsgi.ini