# YOLO Bomber API
![YOLO](https://yolo-storage-v2.s3.amazonaws.com/img/logo-web.svg "YOLO")

YOLO Bomber is just a project i started and finished when i was bored lul and i made it into an API system xD

### Features
* Proxy Input
* Controllable Flood System
* JSON Output

### Setup
```
$  sudo apt update
$  sudo apt install  x11-utils python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools python3-venv xvfb firefox -y
$  cd /opt
$  sudo git clone https://github.com/0x06060606/YOLO-Bomber.git
$  sudo chown -hR www-data:www-data /opt/YOLO-Bomber
$  sudo chmod 775 -Rf /opt/YOLO-Bomber/
$  cd /opt/YOLO-Bomber
$  sudo mv yolo.service /etc/systemd/system/yolo.service
$  python3 -m venv yoloenv
$  source yoloenv/bin/activate
$  pip install wheel uwsgi flask requests flask_restful sqlalchemy bs4 selenium pyvirtualdisplay
$  uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
$  deactivate
$  sudo ln geckodriver /opt/YOLO-Bomber/yoloenv/bin/
$  sudo ln /usr/bin/Xvfb /opt/YOLO-Bomber/yoloenv/bin/
$  sudo ln /usr/bin/xdpyinfo /opt/YOLO-Bomber/yoloenv/bin/
$  sudo systemctl start yolo
$  sudo systemctl enable yolo
$  sudo ln -s /opt/YOLO-Bomber/yoloHTTP /etc/nginx/sites-enabled
$  sudo systemctl restart nginx
$  sudo ufw delete allow 5000
$  sudo ufw allow 'Nginx Full'
```

### Securing
```
$  sudo add-apt-repository ppa:certbot/certbot
$  sudo apt install python-certbot-nginx
$  sudo certbot --nginx -d yolo.soteria.cf
```

License
----
```
MIT License

Copyright (c) 2019 John Bell

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

[@0x06060606](https://twitter.com/0x06060606 "My Twitter")

### API
```
{
  "API": "1.0.0",
  "info": {
    "title": "YOLO-Bomber",
    "version": "1.0.0",
    "contact": {
      "name": "John Bell",
      "url": "https://cyber-sec.engineer/",
      "email": "john@buffer-overflow.tech"
    },
    "description": "YOLO Bomber API"
  },
  "servers": [
    {
      "url": "https://yolo.soteria.cf/bomb",
      "description": "?msg=[MESSAGE]&user=[USER_ID]&count=[COUNT]"
    }
  ]
}
```
