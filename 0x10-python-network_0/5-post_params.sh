#!/bin/bash
#takes in a URL, sends POST  request to the URL,sends variables  and displays the body of the response
curl -d  "email=test%40gmail%2Ecom&subject=I+will+always+be+here+for+PLD" -sX POST $1
