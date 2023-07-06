#!/bin/bash
#curl gets only the header response , grep gets the centent-length line and awk separes the value from the name
curl -sI $1 | grep -iF content-length | awk -F' ' '{print $(NF) }'
