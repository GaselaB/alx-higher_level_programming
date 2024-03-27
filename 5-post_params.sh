#!/bin/bash
# script that takes in a URL, sends a POST request to the passed URL
curl -s "$1" -X POST -d
