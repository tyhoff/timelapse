#!/bin/bash
date=`date +"%Y-%m-%d--%H"`
convert -delay 10 -loop 0 ~/timelapse/timelapse/static/camera/$date* ~/timelapse/timelapse/static/gifs/$date.gif
curl -v -d "image_path=static/gifs/$date.gif&image_type=gif" http://purdue.tyhoffman.com:8000/timelapse/default/api/image.json
