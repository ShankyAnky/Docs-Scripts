#!/bin/bash

#Checking Docker is installed or not

echo "1) Checking docker and docker-compose is availabe or not"

sleep 5

docker --version >> /dev/null

if [ $? -eq "0" ]
then
        echo "Docker is available"
else
        echo "Docker is not available"
        echo "Installing Docker"
        sh docker.sh
fi

sleep 5

#Checking Docker-compose is installed

DOCKERCOMPOSE=/usr/bin/docker-compose
if [ -f "$DOCKERCOMPOSE" ];then
        echo "Docker Compose is installed"
else
        echo "Docker Compose is not Installed"
        sh docker-compose.sh
fi

#ps -ef | grep docker-compose >> /dev/null
#[ $?  -eq "0" ] && echo "docker-compose is available" || echo "docker-compose not available"

#Running Vhost Commands
sudo sysctl -w vm.max_map_count=262144 >> /dev/null
sudo sysctl -w fs.file-max=65536 >> /dev/null

ulimit -n 655536
ulimit -u 4096


sleep 10

#Running Docker Compose

echo "2) Executing docker-compose"

sudo docker-compose -f docker-compose.yaml up -d

#Checking Services

sleep 10

echo "3) Checking whether services are running or not"

sleep 5

sudo docker ps | grep "jenkins" >> /dev/null
jen=$?
if [ "$jen" -eq 0 ]
then
        echo "Jenkins is up"
else
        echo "jenkins is down"
fi
sleep 5
sudo docker ps | grep "postgresql" >> /dev/null
pos=$?
if [ "$pos" -eq 0 ]
then
        echo "postgresql is up"
else
        echo "postgresql is down"
fi
sleep 10
sudo docker ps | grep "sonarqube" >>  /dev/null
sonar=$?
if [ "$sonar" -eq 0 ]
then
        echo "sonarqube is up"
else
        echo "sonarqube is down"
        echo "Solving the issue"
        sudo chmod 777 sonarqube_bundled-plugins sonarqube_conf sonarqube_data sonarqube_extensions
        sudo docker-compose down
        sudo docker-compose -f docker-compose.yaml up -d
fi

#Again Checking Services after solving issues

echo "Please wait! Checking again"
sleep 10

sudo docker ps | grep "sonarqube" >>  /dev/null
sonar1=$?
if [ "$sonar1" -eq 0 ]
then
        echo "Applications are Sucessfully Up and Working"
else
        echo "ERROR"
fi

