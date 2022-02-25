#!/bin/sh
# ------------------------
# 发布镜像
# bin/deploy.sh
# ------------------------

REGISTRY="registry.hub.docker.com"
NAMESPACE="expm02"
VERSION=$(date "+%Y%m%d%H")


function deploy_image() {
    image_name=$1
    remote_url=${NAMESPACE}/${image_name}
    docker tag ${image_name} ${remote_url}
    docker push ${remote_url}:${VERSION}
    docker push ${remote_url}:latest
    echo "Pushed to ${remote_url}"
}


echo "Login to ${REGISTRY} ..."
docker login "https://"${REGISTRY}
image_name=`echo ${PWD##*/}`
deploy_image ${image_name}

docker image ls | grep "${image_name}"
echo "finish ."