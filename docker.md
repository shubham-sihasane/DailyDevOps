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

`docker container run <image-name>:<tag-name>` # Create and start a container from specific image, default tag is latest, `--rm` to remove container once it is stopped, `--rm` for removing a container after stopped automatically

`docker container run --name <container-name> --hostname <container-hostname> <image-name>:<tag-name>` # Create a container with name and set a custom hostname

`docker container exec <container-name/ID> <command>` # Execute a command in a running container

`dcker container start <container-name/ID>` # Start a created or stopped container

`docker container stop <container-name/ID>` # Stop a running container

`docker container stop $(docker container ps)` # Stop all running containers

`docker container rm <container-name/ID> -f` # Remove, delete a stopped running container, `-f`or `--force` for forcefull deleting without stopping a container

`docker container rm $(docker container ps -a)` # Remove all stopped containers

`docker container restart <container-name/ID>` # Restart a running container

`docker container kill <container-name/ID>` # Kill a container

`docker container pause <container-name/ID>` # Pause a running container

`docker container unpause <container-name/ID>` # Unpause a paused container

`docker container rename <old-container-name> <new-container-name>` # Rename an existing container with new name

`docker container logs <container-name/ID>` # Print logs created by a container, `-f` for verbose live logging, `--log-driver json-file`

`docker container top <container-name/ID>` # Print running processes of a container

`docker container inspect <container-name/ID>` # Display detailed information of one or more containers

`docker container port <container-name/ID>` # List port mappings or a specific mapping for the container, `172.17.0.1` docker gateway and further docker containers get IP

`docker container prune` # Remove all stopped containers

`docekr container stats` # Display live stream of containers resource usage statistics

`docker container stat <container-name-ID>` # List statistics of specific container

`docker container attach <container-name-ID>` # Attach to interactive terminal of the running container -> stdin, stdout, stderr streams

`docker container commit <container-name/ID> <new-image-name>` # Create a new image from a container's changes like AWS AMI

`docker container export <container-name/ID> <image.tar>` # Export a conatiner's filesystem as a tar archive

`docker container cp <local-source-path> <container:destination-path>` # Copy files or folders between a local filesystem and container

`docker container diff <container-name/ID>` # Inspect changes to files or directories on a container's filesystem

`docker container update [options] <container-name/ID>` # Update configuration of one or more container

`docker container wait <container-name/ID>` # Block untill one or more containers stop, then print their exit codes

`docker container run -d -p <host-port>:<container-port> <image-name>` # Expose a container port to host port, if host port not mentioned - random available port, -P without any ports info - expose instruction for container port, random port of host

- -d or --detach for running container in background or detached mode
- -p for mapping host port to container port
- -v for mapping local host system filepath inside container filesystem path


#### Manage Images

`docker login <registry-name>` # Authenticate to a registry

`docker logout` # Log out from a registry

`docker search <image-name>:<tag-name>` # Search image in docker hub -> default registry, `--filter stars=10`, many other filters

`docker image ls` # List images

`docker image pull` # Download an image from a registry

`docker.io/library/nginx` # registry/namespace/repo -> docker.io/sihasaneshubham/solar-system:tagname

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

- docker0
- Docker DNS = `27.0.0.11` Containers can communicate with each other via container name or IP

`docker -H=10.123.2.1:2376 --tlsverify run nginx` # Run container on remote host

`docker network create --driver bridge --subnet 182.18.0.0/16 <custom-network>` # Create a custom network

/var/lib/docker/
	containers/
	images/
	volumes/
	overlays2/



#### Manage Volumes
`docker volume ls` # List volumes

`docker create <volume-name>` # Create a custom volume

`docker inspect <volume-name>` # Display detailed information on one or more volumes

`docker rm <volume-name>` # Remove or more volumes

`docker volume prune` # Remove unused local volumes

`docker container run -v /opt/datadir:/var/lib/mysql <mysql-image>`# Create a container by mouting volume

`docker container run --mount type=bind,source=/opt/datadir,target=/var/lib/mysql mysql` # Create container by mouting volume

`docker run --name jenkins -p 8080:8080 -p 50000:50000 --restart=on-failure --memory=100m --cpus=0.5 -v --build-arg <key>:<value> --env <key>:<value> jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk21`# Create a jenkins container, -e, --env, --env-file

#### Restart Policies
- no - Do not start container by default
- always - Restart container
- on-failure - Restart when container exits with a non-zero exit code
- unless-stopped - Always restart except when you manually stop container

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

### Dockerfile

`ADD`	-> Add local or remote files and directories.
`ARG`	-> Use build-time variables.
`CMD`	-> Specify default commands.
`COPY`	-> Copy files and directories.
`ENTRYPOINT`	-> Specify default executable.
`ENV`	-> Set environment variables.
`EXPOSE`	-> Describe which ports your application is listening on.
`FROM`	-> Create a new build stage from a base image.
`HEALTHCHECK`	-> Check a container's health on startup.
`LABEL`	-> Add metadata to an image.
`MAINTAINER`	-> Specify the author of an image.
`ONBUILD`	-> Specify instructions for when the image is used in a build.
`RUN`	-> Execute build commands.
`SHELL`	-> Set the default shell of an image.
`STOPSIGNAL`	-> Specify the system call signal for exiting a container.
`USER`	-> Set user and group ID.
`VOLUME`	-> Create volume mounts.
`WORKDIR`	-> Change working directory.

#### Dockerfile Examples

```
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
```
```
# base defines a base stage that uses the official python runtime base image
FROM python:3.11-slim AS base

# Add curl for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Set the application directory
WORKDIR /usr/local/app

# Install our requirements.txt
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# dev defines a stage for development, where it'll watch for filesystem changes
FROM base AS dev
RUN pip install watchdog
ENV FLASK_ENV=development
CMD ["python", "app.py"]

# final defines the stage that will bundle the application for production
FROM base AS final

# Copy our code from the current folder to the working directory inside the container
COPY . .

# Make port 80 available for links and/or publish
EXPOSE 80

# Define our command to be run when launching the container
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--log-file", "-", "--access-logfile", "-", "--workers", "4", "--keep-alive", "0"]
```

```
FROM node:18-slim

# add curl for healthcheck
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl tini && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/app

# have nodemon available for local dev use (file watching)
RUN npm install -g nodemon

COPY package*.json ./

RUN npm ci && \
 npm cache clean --force && \
 mv /usr/local/app/node_modules /node_modules

COPY . .

ENV PORT=80
EXPOSE 80

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["node", "server.js"]
```
```
# because of dotnet, we always build on amd64, and target platforms in cli
# dotnet doesn't support QEMU for building or running. 
# (errors common in arm/v7 32bit) https://github.com/dotnet/dotnet-docker/issues/1537
# https://hub.docker.com/_/microsoft-dotnet
# hadolint ignore=DL3029
# to build for a different platform than your host, use --platform=<platform>
# for example, if you were on Intel (amd64) and wanted to build for ARM, you would use:
# docker buildx build --platform "linux/arm64/v8" .

# build compiles the program for the builder's local platform
FROM --platform=${BUILDPLATFORM} mcr.microsoft.com/dotnet/sdk:7.0 AS build
ARG TARGETPLATFORM
ARG TARGETARCH
ARG BUILDPLATFORM
RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM"

WORKDIR /source
COPY *.csproj .
RUN dotnet restore -a $TARGETARCH

COPY . .
RUN dotnet publish -c release -o /app -a $TARGETARCH --self-contained false --no-restore

# app image
FROM mcr.microsoft.com/dotnet/runtime:7.0
WORKDIR /app
COPY --from=build /app .
ENTRYPOINT ["dotnet", "Worker.dll"]
```


## Docker Compose

- Usage:  docker compose [OPTIONS] COMMAND
- Define and run multi-container applications with Docker

Management Commands: `bridge` # Convert compose files into another model

attach                  Attach local standard input, output, and error streams to a service's running container
build                   Build or rebuild services
commit                  Create a new image from a service container's changes
config                  Parse, resolve and render compose file in canonical format
cp                      Copy files/folders between a service container and the local filesystem
create                  Creates containers for a service
down                    Stop and remove containers, networks
events                  Receive real time events from containers
exec                    Execute a command in a running container
export                  Export a service container's filesystem as a tar archive
images                  List images used by the created containers
kill                    Force stop service containers
logs                    View output from containers
ls                      List running compose projects
pause                   Pause services
port                    Print the public port for a port binding
ps                      List containers
publish                 Publish compose application
pull                    Pull service images
push                    Push service images
restart                 Restart service containers
rm                      Removes stopped service containers
run                     Run a one-off command on a service
scale                   Scale services 
start                   Start services
stats                   Display a live stream of container(s) resource usage statistics
stop                    Stop services
top                     Display the running processes
unpause                 Unpause services
up                      Create and start containers
version                 Show the Docker Compose version information
volumes                 List volumes
wait                    Block until containers of all (or specified) services stop.
watch                   Watch build context for service and rebuild/refresh containers when files are updated


```
services:
  vote:
    build: 
      context: ./vote
      target: dev
    depends_on:
      redis:
        condition: service_healthy
    healthcheck: 
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 15s
      timeout: 5s
      retries: 3
      start_period: 10s
    volumes:
     - ./vote:/usr/local/app
    ports:
      - "8080:80"
    networks:
      - front-tier
      - back-tier

  result:
    build: ./result
    # use nodemon rather than node for local dev
    entrypoint: nodemon --inspect=0.0.0.0 server.js
    depends_on:
      db:
        condition: service_healthy 
    volumes:
      - ./result:/usr/local/app
    ports:
      - "8081:80"
      - "127.0.0.1:9229:9229"
    networks:
      - front-tier
      - back-tier

  worker:
    build:
      context: ./worker
    depends_on:
      redis:
        condition: service_healthy 
      db:
        condition: service_healthy 
    networks:
      - back-tier

  redis:
    image: redis:alpine
    volumes:
      - "./healthchecks:/healthchecks"
    healthcheck:
      test: /healthchecks/redis.sh
      interval: "5s"
    networks:
      - back-tier

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_USER: "postgres"
      POSTGRES_PASSWORD: "postgres"
    volumes:
      - "db-data:/var/lib/postgresql/data"
      - "./healthchecks:/healthchecks"
    healthcheck:
      test: /healthchecks/postgres.sh
      interval: "5s"
    networks:
      - back-tier

  # this service runs once to seed the database with votes
  # it won't run unless you specify the "seed" profile
  # docker compose --profile seed up -d
  seed:
    build: ./seed-data
    profiles: ["seed"]
    depends_on:
      vote:
        condition: service_healthy 
    networks:
      - front-tier
    restart: "no"

volumes:
  db-data:

networks:
  front-tier:
  back-tier:
```