# How to Install and Use Docker on Ubuntu

<!-- TOC -->

* [docker](#docker)
* [Installing Docker on Ubuntu](#installing-docker-on-ubuntu)
* [Create the Dockerfile for Python Web Apps & Django](#create-the-dockerfile-for-python-web-apps--django)
* [Build the Docker Image](#build-the-docker-image)
* [Run the Docker Container](#run-the-docker-container)
<!-- TOC -->

# docker
Docker is a set of platform as a service product that use OS-level virtualization to deliver software in packages called containers. The service has both free and premium tiers. The software that hosts the containers is called Docker Engine.

# Installing Docker on Ubuntu
command:

    sudo apt install docker.io -y

Run the above command

# Create the Dockerfile for Python Web Apps & Django
Converting our Instructions List to a format Docker understand is this simple. 

To build a Django application is with a Dockerfile in simpler ways, we can create a Docker image. It contains everything using a pipeline.

Here is an example image of how to create a DockerFile text document in the project root. 

![docker_file](https://user-images.githubusercontent.com/109805460/203056815-3f8f80e2-36fa-40a9-a324-0047f8e0391e.png)


# Build the Docker Image

To build the Docker Image, you can use the Docker Build command.

    sudo docker build .
(.) dot will take current working directory. Instead of . we can specify path.

![docker_eg](https://user-images.githubusercontent.com/109805460/203056937-f591b2e9-08ac-42e6-895e-4dc822393325.png)


The above image shows the output after running the command. So we got the docker image name after successful build.

# Run the Docker Container

To run the Docker Container, you can use the Docker Run command.
    
    sudo docker run -it image_name
we need to provide docker image name instead of image_name. 
