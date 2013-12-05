#!/bin/bash
date=`date +"%Y-%m-%d--%H"`

sleep 60

mkdir ~/timelapse/.tempjpg

mogrify -path ~/timelapse/.tempjpg -resize 480x320 ~/timelapse/timelapse/static/camera/$date*

convert -delay 50 -loop 0 ~/timelapse/.tempjpg/* ~/timelapse/timelapse/static/gifs/$date.gif

curl -d "image_path=static/gifs/$date.gif&image_type=gif" http://purdue.tyhoffman.com:8000/timelapse/default/api/image.json

rm -rf ~/timelapse/.tempjpg
