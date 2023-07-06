#!/bin/bash
curl -sI $1 | grep -iF content-length | awk -F' ' '{print $(NF) }'
