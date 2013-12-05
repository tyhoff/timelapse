#Raspberry Pi Timelapse Camera

To set up hardware

1. Motion Sensor sensitivity and time are at extremes. Least amount of time and highest sensitivity. 
2. Motion Sensor is connected to PIN 8.

To download and install the application

```bash
git clone https://github.com/tyhoff/timelapse.git
cd timelapse
```

To make gif creation work you should set up a cron job to run `makegif.sh` every hour
```bash
59 * * * * <path_to_git_proejct>/makegif.sh
```

Start web2py server

```bash
python web2py/web2py.py --ip 0.0.0.0 -a <password>
```

Start timelapse camera

```bash
sudo python camera_timer.py
```

To stop project, you must kill the processes. You can find the PID's by using the below commands

```bash
ps aux | grep web2py
ps aux | grep camera_timer
```



How to access the web2py website

```
http://127.0.0.1:8000/timelapse
```
