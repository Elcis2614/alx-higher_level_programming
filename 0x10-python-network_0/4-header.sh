#!/bin/bash
#takes in a URL, sends a GET request to the URL,sends body variable  and displays the body of the response
curl -s -L -X GET $1"?X%2DSchool%2DUser%2DId=98"
