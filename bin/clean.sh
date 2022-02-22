#!/bin/sh
# ------------------------
# 清理镜像
# bin/clean.sh
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


echo "clean images ..."
image_name=`echo ${PWD##*/}`
del_image ${image_name}
docker image ls | grep "${image_name}"

echo "clean logs ..."
rm -rf ./logs
echo "finish ."