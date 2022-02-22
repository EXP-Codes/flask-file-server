#!/bin/sh
# ------------------------
# 构建镜像
# bin/build.sh
# ------------------------

function del_image([string]$image_name) {
    $image_id = (docker images -q --filter reference=${image_name})
    if(![string]::IsNullOrEmpty(${image_id})) {
        Write-Host "delete [${image_name}] ..."
        docker image rm -f ${image_id}
        Write-Host "done ."
    }
}

function build_image([string]$image_name, [string]$dockerfile) {
    del_image ${image_name}
    docker build -t ${image_name} -f ${dockerfile} .
}


$image_name = (Split-Path $pwd -leaf)
build_image ${image_name} "Dockerfile"
docker-compose build

docker image ls | Where-Object {$_ -like "*${image_name}*"}
Write-Host "finish ."