#!/bin/sh
# ------------------------
# 发布镜像
# bin/deploy.sh
# ------------------------

$REGISTRY = "registry.hub.docker.com"
$NAMESPACE = "expm02"
$VERSION = Get-Date -format "yyMMddHH"


function deploy_image([string]$image_name) {
    $remote_url = "${NAMESPACE}/${image_name}"
    docker tag ${image_name} ${remote_url}
    docker push ${remote_url}:${VERSION}
    docker push ${remote_url}:latest
    Write-Host "Pushed to ${remote_url}"
}


Write-Host "Login to ${REGISTRY} ..."
docker login "https://"${REGISTRY}
$image_name = (Split-Path $pwd -leaf)
deploy_image ${image_name}

docker image ls | Where-Object {$_ -like "*${image_name}*"}
Write-Host "finish ."