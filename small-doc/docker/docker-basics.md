# Docker Basics

---

## Core concepts

| Concept | What it is |
|---------|------------|
| **Image** | A read-only template used to create containers. Built from a Dockerfile. |
| **Container** | A running instance of an image. Isolated process with its own filesystem. |
| **Dockerfile** | A text file with instructions to build an image layer by layer. |
| **Registry** | A storage server for images. Default is Docker Hub (`docker.io`). |
| **Volume** | Persistent storage that lives outside the container filesystem. |
| **Network** | A virtual network connecting containers to each other or to the host. |
| **Layer** | Each Dockerfile instruction adds a cached layer on top of the previous one. |
| **Tag** | A label for a specific version of an image: `nginx:1.25`, `ubuntu:22.04`. |

---

## Images

```bash
docker pull <image>              # download an image
docker pull nginx:1.25           # specific tag
docker images                    # list local images
docker image ls                  # same
docker rmi <image>               # delete an image
docker image rm <image>          # same
docker image prune               # delete dangling (untagged) images
docker image prune -a            # delete all unused images
docker tag <image> <new>         # tag an image
docker inspect <image>           # full metadata in JSON
docker history <image>           # show layers
```

---

## Containers

```bash
docker run <image>               # create and start a container
docker run -d <image>            # detached (background)
docker run -it <image> bash      # interactive with a terminal
docker run --name myapp <image>  # give it a name
docker run --rm <image>          # auto-remove when it stops
docker run -p 8080:80 <image>    # map host port 8080 → container port 80
docker run -e KEY=value <image>  # set environment variable
docker run -v /host:/container <image>  # mount a host directory

docker ps                        # running containers
docker ps -a                     # all containers (incl. stopped)
docker stop <container>          # graceful stop (SIGTERM)
docker kill <container>          # force stop (SIGKILL)
docker start <container>         # restart a stopped container
docker restart <container>       # stop + start
docker rm <container>            # delete a stopped container
docker rm -f <container>         # force delete (even if running)
docker container prune           # delete all stopped containers
```

---

## Interacting with containers

```bash
docker exec -it <container> bash        # open a shell inside a running container
docker exec <container> <cmd>           # run a command without interactive shell
docker logs <container>                 # show logs
docker logs -f <container>              # follow logs in real time
docker logs --tail 50 <container>       # last 50 lines
docker cp <container>:/path ./local     # copy file from container to host
docker cp ./local <container>:/path     # copy file from host to container
docker top <container>                  # running processes inside container
docker stats                            # live resource usage for all containers
docker stats <container>                # resource usage for one container
docker inspect <container>              # full metadata in JSON
docker port <container>                 # show port mappings
docker diff <container>                 # show filesystem changes
```

---

## Dockerfile

```dockerfile
FROM ubuntu:22.04                        # base image (always first)

LABEL maintainer="you@example.com"      # metadata

ENV APP_PORT=8080                        # environment variable

WORKDIR /app                             # set working directory (creates it if missing)

COPY . .                                 # copy files from build context to container
COPY requirements.txt .                  # copy a single file

RUN apt-get update && apt-get install -y python3  # run a command (creates a layer)

EXPOSE 8080                              # document which port the app listens on

VOLUME /data                             # declare a mount point

ENTRYPOINT ["python3"]                   # fixed command, cannot be overridden at runtime
CMD ["app.py"]                           # default arguments to ENTRYPOINT (or default command)
```

> **ENTRYPOINT vs CMD:** `ENTRYPOINT` sets the executable. `CMD` sets default arguments. If only `CMD` is used, it can be fully replaced at `docker run`. When both are set, `CMD` acts as default args to `ENTRYPOINT`.

---

## Building images

```bash
docker build .                           # build from current directory
docker build -t myapp:1.0 .              # with a name and tag
docker build -t myapp:1.0 -f MyDockerfile .  # custom Dockerfile name
docker build --no-cache .                # ignore layer cache
docker build --build-arg KEY=value .     # pass build arguments
```

---

## Volumes

```bash
docker volume create mydata              # create a named volume
docker volume ls                         # list volumes
docker volume inspect mydata             # details
docker volume rm mydata                  # delete
docker volume prune                      # delete all unused volumes

# Use a named volume in a container
docker run -v mydata:/app/data <image>

# Use a host directory (bind mount)
docker run -v /host/path:/container/path <image>

# Read-only bind mount
docker run -v /host/path:/container/path:ro <image>
```

---

## Networks

```bash
docker network ls                        # list networks
docker network create mynet              # create a bridge network
docker network inspect mynet             # details
docker network rm mynet                  # delete
docker network prune                     # delete unused networks

# Connect a container to a network
docker run --network mynet <image>
docker network connect mynet <container>
docker network disconnect mynet <container>
```

Containers on the same custom network can reach each other by **container name**.

---

## Cleanup

```bash
docker container prune       # remove stopped containers
docker image prune           # remove dangling images
docker image prune -a        # remove all unused images
docker volume prune          # remove unused volumes
docker network prune         # remove unused networks
docker system prune          # remove everything unused
docker system prune -a       # remove everything unused incl. all images
docker system df             # disk usage breakdown
```
