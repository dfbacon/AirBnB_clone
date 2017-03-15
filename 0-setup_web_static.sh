#!/usr/bin/env bash
# set up web server for deployment

sudo apt-get install -y nginx

# check and create /data directory
if [ ! -d /data ]; then
    mkdir /data
fi

# check and create /data/web_static directory
if [ ! -d /data/web_static ]; then
    mkdir /data/web_static
fi

# check and create /data/web_static/releases
if [ ! -d /data/web_static/releases ]; then
    mkdir /data/web_static/releases
fi

# check and create /data/web_static/shared
if [ ! -d /data/web_static/shared ]; then
    mkdir /data/web_static/shared
fi

# check and create /data/web_static/releases/test
if [ ! -d /data/web_static/releases/test ]; then
    mkdir /data/web_static/releases/test
fi

# check and create index.html file
if [ ! -f /data/web_static/releases/test/index.html ]; then
    echo "Testing" | sudo tee /data/web_static/releases/test/index.html
fi

ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

sudo sed - i '39 i\tlocation /hbnb_static {\n\t\talias  /data/web_static/curren;\n\t}\n' /etc/nginx/sites-enabled/default

sudo service nginx restart
