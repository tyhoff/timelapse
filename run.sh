#!/bin/bash

# starts the web2py server
nohup python web2py/web2py.py -a cookie --ip 0.0.0.0  &

# takes pictures every so often and changes during motion sensor
nohup sudo python camera_timer.py &
