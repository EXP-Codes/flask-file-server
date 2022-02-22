#!/bin/sh
# ------------------------
# 构建镜像
# bin/build.sh
# ------------------------

function del_image() {
  image_name=$1
  image_id=`docker images -q --filter reference=${image_name}`
  if [ ! -z "${image_id}" ]; then
    echo "delete [${image_name}] ..."
    docker image rm -f ${image_id}
    echo "done ."
  fi
}

function build_image() {
    image_name=$1
    dockerfile=$2
    del_image ${image_name}
    docker build -t ${image_name} -f ${dockerfile} .
}


image_name=`echo ${PWD##*/}`
build_image ${image_name} "Dockerfile"
docker-compose build

docker image ls | grep "${image_name}"
echo "finish ."