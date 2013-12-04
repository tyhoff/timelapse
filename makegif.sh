#!/bin/bash
date=`date +"%Y-%m-%d--%H"`
convert -delay 10 -loop 0 ~/timelapse/timelapse/static/camera/$date* ~/timelapse/static/camera/gifs/$date.gif
