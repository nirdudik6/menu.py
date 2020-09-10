#!/bin/bash

EXIT="no"
while [ $EXIT == "no" ]
do
    echo -e "welcome to to my project!"
    echo -e "select your choice:\n1.pull a specific image\n2.run few ubuntu containers\n3.remove container/image\n4.run web app with specific port\n5.make docker ui\n"
    read CHOICE
    if [ $CHOICE == "1" ]
    then
        echo "which kind of image do you want to pull? (php/ubuntu/centos/nginx)\n"	    
        read IMAGE
        echo "this is the available images..."
        sudo docker search $IMAGE
        echo -e "which image do you want to pull?\n"
        read IMAGE2
        sudo docker pull $IMAGE2

    elif [ $CHOICE == "2" ]
    then
        echo -e "how many containers do you want to run?\n"
        read CONTAINERS
        for i in {1..$CONTAINERS}
        do
        sudo docker run -d ubuntu /bin/bash -c 'while true ; do echo net4u ; sleep 1; done' 2>/dev/null
        done

        sudo  docker ps

    elif [ $CHOICE == "3" ]
    then
        echo -e "enter what do you want to remove: (container/image)\n"
        read REMOVE
        if [ $REMOVE == "image" ]
        then
            echo -e "enter the image's id:\n"
            read ID
            echo "removing..."
            sudo docker rmi $ID

        elif [ $REMOVE == "container" ]
        then
            echo -e "enter the container's id:\n"
            read ID2
            echo "removing..."
            sudo docker rm $ID2
        fi
    elif [ $CHOICE == "4" ]
    then
        echo -e "which port do you want to run?\n"
        read RUN
        sudo docker run -d -p $RUN:8080 adejonge/helloworld
    elif [ $CHOICE == "5" ]
    then
        echo -e "which port do you want to run the docker ui?\n"
        read PORT
        sudo docker run -d -p $PORT:9000 --privileged -v /var/run/docker.sock:/var/run/docker.sock abh1nav/dockerui
    else
        echo "enter 1-4 only!!!"
        continue
    fi
    echo -e "Do you want to exit? yes/no\n"
    read EXIT
echo "thanks and bye bye..."
done


