#!/usr/bin/env bash
# set up web server for deployment

sudo apt-get install -y nginx

# check and create /data directory
if [ ! -d /data ]; then
    sudo mkdir /data
fi

# check and create /data/web_static directory
if [ ! -d /data/web_static ]; then
    sudo mkdir /data/web_static
fi

# check and create /data/web_static/releases
if [ ! -d /data/web_static/releases ]; then
    sudo mkdir /data/web_static/releases
fi

# check and create /data/web_static/shared
if [ ! -d /data/web_static/shared ]; then
    sudo mkdir /data/web_static/shared
fi

# check and create /data/web_static/releases/test
if [ ! -d /data/web_static/releases/test ]; then
    sudo mkdir /data/web_static/releases/test
fi

# check and create index.html file
if [ ! -f /data/web_static/releases/test/index.html ]; then
    echo "<html><head></head><body>Holberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html
fi

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data

prev='location \/ {'
new='location \/hbnb_static\/ {\n\talias \/data\/web_static\/current\n';
sudo sed -i "s/$prev/$new/" /etc/nginx/sites-enabled/default

sudo service nginx restart
