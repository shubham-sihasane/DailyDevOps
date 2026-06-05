`docker -v` OR `docker --version` # Print docker version and quit (client)

`docker version` # Print docker version (client & server)

`cat /etc/*release/*` # About linux system information

`sudo systemctl status docker` # Check status of docker service

`docker` # List all the important docker commands

#### Management Commands:
- builder -> Manage builds
- buildx* -> Docker Buildx
- compose* -> Manage Compose
- container -> Manage containers
- context -> Manage context
- image -> Manage images
- manifest -> manage docker manifests & manifests lists
- network -> Manage plugins
- plugin -> Manage plugins
- system -> Manage Docker
- volume -> Manage volumes

#### Swarm Commands
- swarm -> Manage Swarm

`docker <command> help` # Help page for command

`docker system info` # Display system wide information about docker

`docker system df` # Show docker disk usage

`docker system events` # Display real time events from docker server

`docker system prune` # Remove unused docker data, remove all stopped containers, unused docker networks by containers, all dangling images, unused build cache

#### Manage Containers
`docker container ls` # List containers

`docker container ps -q` # List running containers, `-q` for ID's only

`docker container ps -aq` # List running and stopped, all containers, `-q` for ID's only

`docker container create <image-name>` # Create a container

`docker container run <image-name>:<tag-name>` # Create and start a container from specific image, default tag is latest

`docker container exec <container-name/ID> <command>` # Execute a command in a running container

`dcker container start <container-name/ID>` # Start a created or stopped container

`docker container stop <container-name/ID>` # Stop a running container

`docker container stop $(docker container ps)` # Stop all running containers

`docker container rm <container-name/ID> -f` # Remove, delete a stopped running container, `-f` for forcefull deleting without stopping a container

`docker container rm $(docker container ps -a)` # Remove all stopped containers

`docker container restart <container-name/ID>` # Restart a running container

`docker container kill <container-name/ID>` # Kill a container

`docker container pause <container-name/ID>` # Pause a running container

`docker container unpause <container-name/ID>` # Unpause a paused container

`docker container rename <old-container-name> <new-container-name>` # Rename an existing container with new name

`docker container logs <container-name/ID>` # Print logs created by a container

`docker container top <container-name/ID>` # Print running processes of a container

`docker container inspect <container-name/ID>` # Display detailed information of one or more containers

`docker container port <container-name/ID>` # List port mappings or a specific mapping for the container, `172.17.0.1` docker gateway and further docker containers get IP

`docker container prune` # Remove all stopped containers

`docekr container stats` # Display live stream of container/s resource usage statistics

`docker container attach <container-name-ID>` # Attach to interactive terminal of the running container -> stdin, stdout, stderr streams

`docker container commit <container-name/ID> <new-image-name>` # Create a new image from a container's changes like AWS AMI

`docker container export <container-name/ID> <image.tar>` # Export a conatiner's filesystem as a tar archive

`docker container cp <source-path> <container:destination-path>` # Copy files or folders between a local filesystem and container

`docker container diff <container-name/ID>` # Inspect changes to files or directories on a container's filesystem

`docker container update [options] <container-name/ID>` # Update configuration of one or more container

`docker container wait <container-name/ID>` # Block untill one or more containers stop, then print their exit codes

# `docker container run -d -p <host-port>:<container-port> <image-name>`

- -d for running container in background or detached mode
- -p for mapping host port to container port
- -v for mapping local host system filepath inside container filesystem path


#### Manage Images

`docker login` # Authenticate to a registry

`docker logout` # Log out from a registry

`docker search <image-name>:<tag-name>` # Search image in docker hub -> default registry

`docker image ls` # List images

`docker image pull` # Download an image from a registry



`docker image build -t <image-name>:<tag-name> -f <Dockerfile-path> <build-context>` OR `docker image build .` # Build an image from Dockerfile with reference to build 

`docker image build --build-arg <API=secret-key -t <image-name>:<tag-name>  .` # This will leak the secret info in image history, Not recommended for sensitive information

`docker tag <old-image-name>:<tag-name> <new-image-name>:<tag-name>` # Tag or rename an existing image

`docker image push <registry:/image-name>:<tag-name>` # Upload an image to registry

`docker image inspect <image-name>:<tag-name>` # Display detailed information on one or more images

`docker image history --no-trunc <image-name>:<tag-name>` # Show the history of an image, `--no-trunc` for detailed history not just layers

`docker image import <image.tar>` # Import the contents from a tarball to create a filesystem image

`docker image save <image-name>:<tag-name> <image.tar>` # Save one or more images to a tar archive

`docker image load <image.tar>` # Load an image from a tar archive

`docker image rm <image-name>:<tag-name>` OR `docker rmi <image-name>:<tag-name>`# Remove one or more images

`docker image prune` # Remove unused images

#### Manage Networks
`docker network ls` # List networks

# `docker network create [options] <custom-network>` # Create a custom network

`docker network inspect <network-name>` # Display detailed information on one or more networks

`docker network connect [options] <network-name> <container-name>` # Connect a container to network

`docker network disconnect [options] <network-name> <container-name>` # Disconnect a container from network

`docker network rm <network-name>` # Remove one or more networks

`docker network prune` # Remove one or more networks


#### Manage Volumes
`docker volume ls` # List volumes

`docker create <volume-name>` # Create a custom volume

`docker inspect <volume-name>` # Display detailed information on one or more volumes

`docker rm <volume-name>` # Remove or more volumes

`docker volume prune` # Remove unused local volumes

`docker container run -v /opt/datadir:/var/lib/mysql <mysql-image>`# Create a container by mouting volume

`docker container run --mount type=bind,source=/opt/datadir,target=/var/lib/mysql mysql` # Create container by mouting volume

`docker run -p 8080:8080 -p 50000:50000 --restart=on-failure -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk21`# Create a jenkins containe


#### PROBLEMS with Traditional Docker Builds - Legacy image builder issues
- *Package Re-download* -> every build, every layer from sratch, time consuming and unnecessary
- *Secrets Leak* -> No matter the work around
- *Architecture Lock-In* -> amd64/arm64, image built on intel amd64 wont work arm64 like apple silicon
- *Sequential Stages* -> Independent stages running sequentially though can be run parallel, time consuming

#### Secrets Leak Issues - Passing secret info while building image
- *Build Argument*
  - Passing secret using`--build-arg` is safe as it's runtime of building image but still secrets information remains in layers of image, easy expose
- *Env*
  - Passing secret as a part of image itself using `ENV` argument is worst way to expose as it will remain in image layers
- *Copy and Delete*
  - Copy secret into image and delete again from image using separate layers, easy expose from image layers and tarball extration
- *Multi-Stage Build*
  - Passing secret in one stage and using it in another stage, little safer but still secret remains available for exposure in earlier stages and filesystem of host system 

#### Solution -> Docker BuildKit -> buildx
Docker launched Docker BuildKit to solve all above issues and it's default with docker version 23.0
- Content-hashed caching
- Four new capabilities


#### Manage Buildx
Extended build capabilities with BuildKit
Usage:  docker buildx [OPTIONS] COMMAND

Extended build capabilities with BuildKit

Options:
      --builder string   Override the configured builder instance
  -D, --debug            Enable debug logging

Management Commands:
  dap         Start debug adapter protocol compatible debugger
  history     Commands to work on build records
  imagetools  Commands to work on images in registry
  policy      Commands for working with build policies

Commands:
  bake        Build from a file
  build       Start a build
  create      Create a new builder instance
  dial-stdio  Proxy current stdio streams to builder instance
  du          Disk usage
  inspect     Inspect current builder instance
  ls          List builder instances
  prune       Remove build cache
  rm          Remove one or more builder instances
  stop        Stop builder instance
  use         Set the current builder instance
  version     Show buildx version information

Run 'docker buildx COMMAND --help' for more information on a command.

#### Dockerfile Examples

FROM ubuntu
RUN apt-get update -y
RUN apt-get install python3-flask -y
COPY app.py /opt/app.py
ENV FLASK_APP=/opt/app.py
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]

FROM alpine
RUN apt-get update -y && \
    apt-get install python-flask
