#!/bin/python3
import os
import subprocess
import sys
import augeas

def change_emp():
    os.system('sudo ifconfig eth0 down')
    new_ip=input("enter your new enp0s8's ip:\n")
    os.system('sudo ifconfig eth0 + new_ip')
    os.system('sudo ifconfig eth0 up')

def add_route():
    ip_route=input("enter your ip route that you want to add:\n")
    mask=input("enter your mask number:\n")
    gateway=input("enter your gateway ip:\n")
    os.system('route ADD + ip route + MASK + mask + gateway')

def change_hostname():
    os.system('apt-get install systemd -y')
    new_hostname=input("enter your new hostname:\n")
    os.system('sudo hostnamectl set-hostname + new_hostname')
    os.system('hostnamectl')
    print("this is your new hostname:\n")
    os.system('hostname')

def change_etc():
    host=input("enter the new host:\n")
    remote_ip=input("enter the new ip:\n")
    SetHostAt(remote_ip)

def change_root():
    print("lets change your root password!")
    dilema=input("are you sure you want to change your root password? y/n\n")
    if (dilema=="y"):
        os.system('sudo passwd root')
        print("DONE!")
    elif (dilema=="n"):
        print("ok,you don't want to change...")

def enable_ssh():
    os.system('sudo sed -i "s/#PermitRootLogin prohibit-password/PermitRootLogin yes/" /etc/ssh/sshd_config')
    os.system('sudo service ssh restart')

def SetHostAt(remote_ip):
    MYROOT = '/'
    a = augeas(root=MYROOT)
    matches=input("Do you have an exists records? yes/no\n")
    if (matches=="yes"):
        index = matches[0].split('/')[4]
        record_exists = True
        print(index)
    elif (matches=="no"):
        record_exists = False
        index = len(a.match("/files/etc/hosts/*"))
        print(index)
    a.set("/files/etc/hosts/%s/ipaddr" % index, remote_ip)
    a.set("/files/etc/hosts/%s/canonical" % index, host)
    a.save()
    msg = "set host ip to %s" % remote_ip
    init("server checker")
    notification("server checker", mgs).show()


while(True):
    choice=input("enter your  choice: \n1.change emp0s8\n2.add a route\n3.change hostname\n4.change etc/hosts\n5.change root password\n6.enable ssh to root\n")
    if (choice=="1"):
        change_emp()
    elif (choice=="2"):
        add_route()
    elif (choice=="3"):
        change_hostname()
    elif (choice=="4"):
        change_etc()
    elif (choice=="5"):
        change_root()
    elif (choice=="6"):
        enable_ssh()
    else:
        print("choose only 1-5!!!")
        continue
    if (input("do you want to exit? y/n\n") == "y"):
        break
print("thanks and bye bye...")
