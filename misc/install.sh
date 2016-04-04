#!/bin/bash
set -xe

echo "Updating system filee..."
sudo apt-get update

echo "Installing core dependencies..."
sudo apt-get install -y python-dev python-pip git-core

echo "Installing ansible installer..."
sudo pip install ansible==2.0.1.0

echo "Pulling SYNC CORE !!!"
ansible localhost -m git -a "repo=git://github.com/Geo-Joy/sync-pi-ose.git dest=/home/pi/sync"
cd /home/pi/sync/misc/ansible

echo "Running ansible..."
ansible-playbook system.yml
ansible-playbook sync.yml

echo "Downloading rpi3-wifi-setup..."
git -a "repo=git://github.com/tonypius/rpi3-wifi-setup.git dest=/home/pi/rpi3-wifi-setup"

echo "Moving to /home/pi/rpi3-wifi-setup..."
cd /home/pi/rpi3-wifi-setup

echo "Configiring wifi-ap & boot resolution config..."
./install.sh
