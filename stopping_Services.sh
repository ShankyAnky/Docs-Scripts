#!/bin/bash

echo "Stopping All Services"

sudo docker-compose down
sudo apt-get purge -y docker-engine docker docker.io docker-ce  
sudo apt-get autoremove -y --purge docker-engine docker docker.io docker-ce
sudo rm -rf -v ! (*.yaml|*.sh)

echo "All Services stopped and Folders Deleted"

