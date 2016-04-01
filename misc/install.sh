#!/bin/bash
set -xe
sudo apt-get update
sudo apt-get install -y python-dev python-pip git-core
sudo pip install ansible==2.0.1.0

ansible localhost -m git -a "repo=git://github.com/wireload/sync-ose.git dest=/home/pi/sync"
cd /home/pi/sync/misc/ansible
ansible-playbook system.yml
ansible-playbook sync.yml
