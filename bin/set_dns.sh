#!/bin/bash
# ------------------------
# 设置本地域名解析
# （把测试环境的域名解析到本地局域网 IP，不能为 127.0.0.1）
#  (此脚本需要 sudo 执行，语法仅适用于 mac 系统)
# sudo bin/set_dns.sh
# ------------------------

DNS_FILE="/etc/hosts"
DOMAIN="flask.local.com"
LOCAL_IP=`ifconfig en0 | grep 'netmask' | awk '{print $2}'`

# 修改本地 hosts 文件
if [ `grep -c "${DOMAIN}" ${DNS_FILE}` -ne '0' ];then
    FROM_REG="^[0-9.]* ${DOMAIN}$"
    TO_STR="${LOCAL_IP} ${DOMAIN}"
    sed -i '' -E "s/${FROM_REG}/${TO_STR}/" ${DNS_FILE}
else
    echo "${LOCAL_IP} ${DOMAIN}" >> ${DNS_FILE}
fi

# 修改 bb-iam-bam-admin 模块的 docker-compose DNS 解析
echo "LOCAL_DNS=${LOCAL_IP}" > ${ENV_FILE}


echo "${LOCAL_IP} ${DOMAIN}"
echo "Finish ."
