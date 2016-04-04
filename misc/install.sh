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


mkdir /home/pi/rpi3-wifi-setup
echo "Moving to /home/pi/rpi3-wifi-setup..."
cd /home/pi

echo "Downloading rpi3-wifi-setup..."
git clone http://github.com/tonypius/rpi3-wifi-setup.git

echo "Configuring wifi-ap & boot resolution ..."
./install.sh
