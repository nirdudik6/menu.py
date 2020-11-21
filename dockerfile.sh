 #!/bin/bash

sudo docker build /home/nir/Desktop/dockerfiles/
echo "done!" 
sudo docker images
echo -e "enter the image's id:\n"
read id 
sudo docker run -d -p 80:80 $id
echo "done!"
sudo docker images
sudo docker ps -a
echo "lets check the connection to port 80"
curl -v telnet://127.0.0.1:80
