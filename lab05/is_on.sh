#!/bin/bash

# 检查是否提供主机参数
if [ -z "$1" ]; then
    exit 1
fi

# ping主机（只发 1 个包，超时 1 秒，不显示输出）
ping -c 1 -W 1 "$1" > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "OK"
else
    echo "Host is not reachable"
fi