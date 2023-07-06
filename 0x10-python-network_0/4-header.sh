#!/bin/bash
#takes in a URL, sends a GET request to the URL,sends body variable  and displays the body of the response
curl -s -L $1 -H "X-School-User-Id=98"
