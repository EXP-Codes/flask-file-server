#!/bin/sh
# ------------------------
# 清理镜像
# bin/clean.sh
# ------------------------

function del_image([string]$image_name) {
    $image_id = (docker images -q --filter reference=${image_name})
    if(![string]::IsNullOrEmpty(${image_id})) {
        Write-Host "delete [${image_name}] ..."
        docker image rm -f ${image_id}
        Write-Host "done ."
    }
}


Write-Host "clean images ..."
$image_name = (Split-Path $pwd -leaf)
del_image ${image_name}

docker image ls | Where-Object {$_ -like "*${image_name}*"}
Write-Host "finish ."