#Raspberry Pi Timelapse Camera

To set up hardware

1. Motion Sensor sensitivity and time are at extremes. Least amount of time and highest sensitivity. 
2. Motion Sensor is connected to PIN 8.

To download

```bash
git clone https://github.com/tyhoff/timelapse.git
```

Install dependencies
```bash
apt-get install imagemagick
```

To make gif creation work you should set up a cron job to run `makegif.sh` every hour
```bash
59 * * * * <path_to_git_proejct>/makegif.sh
```

Start services
```bash
./run.sh
```

How to access the web2py website

```
http://<raspberry_pi_IP>:8000/timelapse
```

To stop project, you must kill the processes. You can find the PID's by using the below commands

```bash
ps aux | grep web2py
ps aux | grep camera_timer
```


