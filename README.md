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
$  sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
$  sudo apt install python3-venv
$  cd /opt
$  sudo git clone https://github.com/0x06060606/YOLO-Bomber.git
$  sudo chown -hR www-data:www-data /opt/YOLO-Bomber
$  sudo chmod 775 -Rf /opt/YOLO-Bomber/
$  cd /opt/YOLO-Bomber
$  sudo mv yolo.service /etc/systemd/system/yolo.service
$  python3 -m venv yoloenv
$  source yoloenv/bin/activate
$  pip install wheel uwsgi flask requests flask_restful sqlalchemy bs4
$  uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
$  deactivate
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
$  sudo certbot --nginx -d [DOMAIN]
```

License
----
[TBA]

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
      "url": "/bomb",
      "description": "?msg=[MESSAGE]&user=[USER_ID]&count=[COUNT]"
    }
  ]
}
```
