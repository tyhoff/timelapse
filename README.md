#Raspberry Pi Timelapse Camera

To download and install the application

```bash
git clone https://github.com/tyhoff/timelapse.git
cd timelapse
bash install.sh
```

Start web2py server

```bash
python web2py/web2py.py --ip 0.0.0.0 -a <password>
```

Start timelapse camera

```bash
sudo python TimeLapse.py
```


How to access the web2py website

```
http://127.0.0.1:8000/timelapse
```
