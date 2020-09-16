#!/bin/python3

import boto3
import paramiko
import os

def menu():
    while(True):
        choice=input("enter your  choice: \n1.installation & update machine\n2.deploy machine\n3.destroy machin\n4.install nagios server\n5.install awscli &  config credentials\n6.exchange keys between 2 machines\n")
        if (choice=="1"):
            installation_update()
        elif (choice=="2"):
            deploy_machine()
        elif (choice=="3"):
            destroy_machine()
        elif (choice=="4"):
            install_nagios()
        elif (choice=="5"):
            awscli_install()
        elif (choice=="6"):
            exchange_keys()
        else:
            print("choose only 1-6!!!")
            continue
        if (input("do you want to exit? y/n\n") == "y"):
            break
    print("thanks and bye bye...")


def installation_update():
    using=input("Do you want to do it local or remote?\n")
    if (using=="remote"):
        ip=input("enter your ip address:\n")
        install=input("enter ubuntu or centos:\n")
        nir_paramiko(ip,os)
    elif (using=="local"):
        os.system('sudo apt-get update -y')
        os.system('sudo apt-get upgrade -y')
        os.system('sudo apt-get dist-upgrade -y')
        os.system('sudo reboot')
        os.system('sudo apt-get install foo')


def deploy_machine():

    ec2 = boto3.resource('ec2')

    instances = ec2.create_instances(
        ImageId=input("enter the ImageId"),
        MinCount=1,
        MaxCount=int(input("how many instances do you want:\n")),
        InstanceType=input("enter your instance's type:\n"),
        KeyName=input("enter your Keyname:\n")
    )

def destroy_machine():

    instances=input("enter the ids of the instances that you want to stop:\n")
    ids = [instances]
    ec2 = boto3.resource('ec2')

    ec2.instances.filter(InstanceIds = ids).terminate()



def install_nagios():
    os.system('sudo apt-get update -y')
    os.system('sudo apt-get install wget build-essential unzip openssl libssl-dev')
    os.system('sudo apt-get install apache2 php libapache2-mod-php php-gd libgd-dev')
    print("creating new username that name nagios")
    print("creating new group that name nagcmd")
    os.system('sudo adduser nagios')
    os.system('sudo addgroup nagcmd')
    os.system('sudo usermod -a -G nagcmd nagios')
    os.system('sudo usermod -a -G nagcmd www-data')
    os.system('cd /opt/')
    os.system('wget https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.4.5.tar.gz')
    os.system('tar xzf nagios-4.4.5.tar.gz')
    os.system('sudo ./configure --with-command-group=nagcmd')
    os.system('sudo make all')
    os.system('sudo make install')
    os.system('sudo make install-init')
    os.system('sudo make install-daemoninit')
    os.system('sudo make install-config')
    os.system('sudo make install-commandmode')
    os.system('sudo make install-exfoliation')
    os.system('cp -R contrib/eventhandlers/ /usr/local/nagios/libexec/')
    os.system('chown -R nagios:nagios /usr/local/nagios/libexec/eventhandlers')
    print("now creating an apache configuration file...")
    os.system('sudo htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin')
    os.system('sudo a2enconf nagios')
    os.system('sudo a2enconf cgi rewrite')
    os.system('sudo service apache2 restart')
    print("installing nagios plugins...")
    os.system('cd /opt')
    os.system('wget http://www.nagios-plugins.org/download/nagios-plugins-2.2.1.tar.gz')
    os.system('tar xzf nagios-plugins-2.2.1.tar.gz')
    os.system('cd nagios-plugins-2.2.1')
    os.system('sudo ./configure --with-nagios-user=nagios --with-nagios-group=nagios --with-openssl')
    os.system('sudo ')
    os.system('sudo make install')
    print("verify the nagios installation...")
    os.system('/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg')
    os.system('sudo service nagios start')
    os.system('sudo systemctl enable nagios')
    os.system('"http://10.0.0.22/nagios"')
    print("finsihed! search 10.0.0.22 to see the results!")



def awscli_install():
    using=input("Do you want to use local or remote?\n")
    if (using=="local"):
        os.system('curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"')
        os.system('unzip awscli-bundle.zip')
        os.system('sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws')
    elif (using=="remote"):
        ip=input("enter the ip:\n")
        port=22
        username=input("enter your username:\n")
        password=input("enter your password:\n")
        command = "aws configure --profile user1"

        ssh=paramiko.SSHClient()
        ssh.set_missig_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,username,password)
        stdin,stdout,stderr=ssh.exec_command(command)
        stdin.write(id+ '\n')
        stdin.write(key+ '\n')
        stdin.write('us-east-1'+ '\n')
        stdin.write(''+ '\n')
        stdin.flush()
        print(stdout.read().decode())
        ssh.close()


def exchange_keys():
    ssh-keygen
    username=input("enter your username:\n")
    ip=input("enter your ip address:\n")
    os.system('sudo ssh-copy-id + username + @ + ip')
    os.system('sudo systemctl reload sshd.service')


def nir_paramiko(ip,os):

    if (os=="centos"):
        port=int(input("enter your port:\n"))
        username=int(input("enter your username:\n"))
        password=int(input("enter your password:\n"))
        cmd='sudo yum update -y'

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,username,password)
        #stdin,stdout,stderr=
        ssh.exec_command(cmd)
        #outlines=stdout.readlines()
        #resp=''.join(outlines)
        #print(resp)

    elif (os=="ubuntu"):
        port=int(input("enter your port:\n"))
        username=int(input("enter your username:\n"))
        password=int(input("enter your password:\n"))
        cmd='sudo apt-get update -y'

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,username,password)
        #stdin,stdout,stderr=
        ssh.exec_command(cmd)
        #outlines=stdout.readlines()
        #resp=''.join(outlines)
        #print(resp)

