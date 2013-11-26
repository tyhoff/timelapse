# download web2py and place it in the timelapse folder
git clone https://github.com/web2py/web2py

# move the timelapse application to the web2py/applications/
mv timelapse web2py/applications/

# starts the web2py server
python web2py/web2py.py -a cookie --ip 0.0.0.0

# takes pictures every so often and changes during motion sensor
sudo python TimeLapse.py
