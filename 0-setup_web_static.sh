#!/usr/bin/env bash
#Set up web servers to deploy web_static

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

echo "
<html>
        <head>
                <title>Test page</title>
        </head>
        <body>
                <h2>Test page for Static deployment</head>
        </body>
</html>" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/

sudo sed -i '/server_name _;/a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart

exit 0
