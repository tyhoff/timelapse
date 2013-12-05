import subprocess
import datetime
import os
import threading
import time
import urllib
import urllib2

PI=1

INTERVAL_NORMAL = 300 # seconds
INTERVAL_MOTION = 30 # seconds

IMAGES_WEB2PY_PATH = 'static/camera/'
WEB2PY_APP_PATH = 'timelapse/'
WEB2PY_URL = 'http://127.0.0.1:8000/timelapse/'

timer_start     = time.time()

if PI: 
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    global PIR_PIN
    PIR_PIN = 8
    GPIO.setup(PIR_PIN, GPIO.IN)



def popenAndCall(onExit, onExit_args, popenArgs):
    """
    Runs the given args in a subprocess.Popen, and then calls the function
    onExit when the subprocess completes.
    onExit is a callable object, and popenArgs is a list/tuple of args that 
    would give to subprocess.Popen.
    """
    def runInThread(onExit, onExit_args, popenArgs):
        proc = subprocess.Popen(popenArgs)
        proc.wait()
        onExit(*onExit_args)
        return
    thread = threading.Thread(target=runInThread, args=(onExit, onExit_args, popenArgs))
    thread.start()
    return thread


        
def takePicture():
    image_web2py_path = IMAGES_WEB2PY_PATH + datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S') + '.jpg'
    image_unix_path = WEB2PY_APP_PATH + image_web2py_path

    postPicArgs = [image_web2py_path]
    cmdArgs = [ 'raspistill', 
                '--nopreview',
                '--timeout', '0',
                '--quality', '75',
                '--width', '640',
                '--height', '480',
                '--output', image_unix_path ]

    popenAndCall(postPic, postPicArgs, cmdArgs)


def postPic(image_path):
    url = WEB2PY_URL  + 'default/api/image.json'
    values = {'image_path' : image_path, 'image_type' : 'camera'}

    print "IMAGE_PATH: " + image_path

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()
    pass



while True:

    if GPIO.input(PIR_PIN):
        if (time.time() - timer_start) > INTERVAL_MOTION:
            takePicture()
            #print "INTERVAL_MOTION"
            timer_start = time.time()
        else:
            pass
    else:
        if (time.time() - timer_start) > INTERVAL_NORMAL:
            takePicture()
            #print "INTERVAL_NORMAL"
            timer_start = time.time()
        else:
            pass
    time.sleep(.01)


