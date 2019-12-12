#!/bin/bash


sudo curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose

sudo chmod +x /usr/bin/docker-compose



DOCKERCOMPOSE=/usr/bin/docker-compose
if [ -f "$DOCKERCOMPOSE" ];then
        echo "Docker Compose is now installed"
else
        echo "Docker Compose is not Installed"
fi

docker-compose --version

