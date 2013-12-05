import subprocess
import datetime
import os
import threading
import time
import urllib
import urllib2

PI=1

INTERVAL_NORMAL = 15 # seconds
INTERVAL_MOTION = 10 # seconds

# MODE_NORMAL = 1
# MODE_MOTION = 2

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
                '--height', '1024',
                '--width', '768',
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

    print 'TIME: %f' % (time.time() - timer_start)

    time.sleep(1)


# curl -d "name=Bob" http://127.0.0.1:8000/timelapse/default/api/person.json

# b.define_table('image',
#                 Field('image_path', default = URL('static/camera/')),
#                 Field('upload_date', 'datetime', default = request.now))




# import time
# import RPi.GPIO as GPIO
# # GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD)

# pir_pin = 8

# GPIO.setup(pir_pin, GPIO.IN)         # activate input

# while True:
#     if GPIO.input(pir_pin):
#         print('PIR ALARM!')
#     else:
#         print('NOPE')
#     time.sleep(1)
