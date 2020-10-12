#!/bin/bash

EXIT="no"
while [ $EXIT == "no" ]
do
    echo -e "welcome to to my docker project!"
    echo -e "select your choice:\n1.download/update/delete image\n2.create new container\n3.check with curl\n"
    read CHOICE
    if [ $CHOICE == "1" ]
    then
        echo -e "Do you want to download/update/delete?\n"
        read DO
        if [ $DO == "download" ]
        then
            echo -e "which kind of image do you want to download? (dockerui/jenkins/centos/nginx)\n"	    
            read IMAGE
            echo "this is the available images:"
            sudo docker search $IMAGE
            echo -e "which image's ID do you want to download?\n"
            read download
            sudo docker pull $download
            echo "DONE!"
        elif [ $DO == "update" ]
        then
            echo -e "There are the downloaded images:\n"
            sudo docker images
            echo -e "which image's ID do you want to update?\n"
            read update
            sudo docker rmi $update
            sudo docker pull $update
            echo "DONE!"
        elif [ $DO == "delete" ]
        then
            echo -e "There are the downloaded images:\n"
            sudo docker images
            echo -e "which image's ID do you want to delete?\n"
            read delete
            sudo docker rmi $delete
            echo "DONE!"
        fi
    elif [ $CHOICE == "2" ]
    then
        echo -e "how many containers do you want to create?\n"
        read CONTAINERS
        for i in $( eval echo {1..$CONTAINERS} )
        do
            echo -e "which root do you want to use?\n"
            read root
            echo -e "which type of container do you want to create? (centos,jenkins,'adejonge/helloworld'/dockerui/,nginx\n"
            read machine
            if [ $machine == "dockerui" ]
            then
                sudo docker pull abh1nav/dockerui:latest
                sudo docker run -d -p $root:9000 -v /var/run/docker.sock:/docker.sock --name dockerui abh1nav/dockerui:latest -e="/docker.sock"
                echo "DONE!"

            else
                sudo docker run -d -p $root:8080 $machine
                echo "done!"
            fi
        done
        sudo docker ps

    elif [ $CHOICE == "3" ]
    then
        echo -e "let's check if it works...\n"
        echo -e "Enter the IP Adress of the container you want to check: (for example:10.0.0.24:8080)\n"
        read IP
        curl -v telnet://$IP
    else
        echo "enter 1-3 only!!!"
        continue
    fi
    echo -e "Do you want to exit? yes/no\n"
    read EXIT
done
