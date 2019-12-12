#!/bin/bash


sudo apt update

sudo apt install apt-transport-https ca-certificates curl software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

sudo apt update

sudo apt install -y docker-ce

echo ${USER}

sudo usermod -aG docker ${USER}

ps -ef | grep docker | grep -v grep >> /dev/null
if [ $? -eq "0" ]
then
        echo "Docker is available now"
else
        echo "Docker is still  not available! 'ERROR'"
fi

