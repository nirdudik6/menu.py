#!/bin/bash

echo -e "\n[gui]\n192.168.1.1\n192.168.1.2" >> sudo nano /etc/ansible/hosts
ansible -m ping gui
ansible gui -b -m apt -a 'name=tcpdump state=present'
ansible gui -a  'touch 1.txt 2.txt 3.txt 4.txt 5.txt'
ansible gui -a  'tar -zcvf nir.tgz 1.txt 2.txt 3.txt 4.txt 5.txt'
ansible gui -a  'rm -r nir.tgz'
ansible gui -a  'rm  1.txt 2.txt 3.txt 4.txt 5.txt'
ansible gui -b -m apt -a 'name=apache2 state=present'
ansible gui -b -m service -a 'name=apache2 enabled=true'
ansible gui -b -m service -a 'name=apache2 state=started'
ansible gui -b -m command 'reboot'
