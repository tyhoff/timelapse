#!/bin/bash

# download web2py and place it in the timelapse folder
git clone https://github.com/web2py/web2py

# move the timelapse application to the web2py/applications/
ln -s $PWD/timelapse $PWD/web2py/applications/timelapse

# install imagemagick dependency (for gif creation)
sudo apt-get install imagemagick

