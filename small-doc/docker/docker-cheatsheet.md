# Docker — Quick Cheat Sheet

---

## Images

| Command | Description |
|---------|-------------|
| `docker pull <image>` | Download an image |
| `docker pull <image>:<tag>` | Specific tag |
| `docker images` | List local images |
| `docker rmi <image>` | Delete an image |
| `docker image prune` | Delete dangling images |
| `docker image prune -a` | Delete all unused images |
| `docker tag <image> <new>` | Tag an image |
| `docker inspect <image>` | Full metadata |
| `docker history <image>` | Show layers |
| `docker save <image> \| gzip > img.tar.gz` | Export image to file |
| `docker load < img.tar.gz` | Import image from file |

---

## Containers

| Command | Description |
|---------|-------------|
| `docker run <image>` | Create and start a container |
| `docker run -d <image>` | Run in background |
| `docker run -it <image> bash` | Interactive shell |
| `docker run --name <name> <image>` | Named container |
| `docker run --rm <image>` | Auto-remove on stop |
| `docker run -p 8080:80 <image>` | Map port host→container |
| `docker run -e KEY=val <image>` | Set env variable |
| `docker run -v /host:/ctr <image>` | Bind mount |
| `docker run -v vol:/ctr <image>` | Named volume |
| `docker run --network <net> <image>` | Attach to network |
| `docker run --restart unless-stopped <image>` | Auto-restart policy |
| `docker run --memory 512m --cpus 1.5 <image>` | Resource limits |
| `docker run --user 1000:1000 <image>` | Run as specific user |
| `docker run --read-only <image>` | Read-only filesystem |
| `docker run --init <image>` | Proper PID 1 / signal handling |
| `docker ps` | Running containers |
| `docker ps -a` | All containers |
| `docker ps -q` | IDs only |
| `docker stop <container>` | Graceful stop |
| `docker kill <container>` | Force stop |
| `docker start <container>` | Start a stopped container |
| `docker restart <container>` | Stop + start |
| `docker rm <container>` | Delete stopped container |
| `docker rm -f <container>` | Force delete |
| `docker container prune` | Delete all stopped containers |
| `docker rename <old> <new>` | Rename a container |

---

## Interacting with containers

| Command | Description |
|---------|-------------|
| `docker exec -it <ctr> bash` | Open a shell inside a running container |
| `docker exec <ctr> <cmd>` | Run a command |
| `docker logs <ctr>` | Show logs |
| `docker logs -f <ctr>` | Follow logs |
| `docker logs --tail 50 <ctr>` | Last 50 lines |
| `docker logs --since 1h <ctr>` | Logs from the last hour |
| `docker cp <ctr>:/path ./local` | Copy file from container |
| `docker cp ./local <ctr>:/path` | Copy file to container |
| `docker top <ctr>` | Processes inside container |
| `docker stats` | Live resource usage |
| `docker stats <ctr>` | Resource usage for one container |
| `docker inspect <ctr>` | Full metadata |
| `docker port <ctr>` | Port mappings |
| `docker diff <ctr>` | Filesystem changes since start |
| `docker export <ctr> > backup.tar` | Export container filesystem |

---

## Building

| Command | Description |
|---------|-------------|
| `docker build .` | Build from current directory |
| `docker build -t name:tag .` | Build with a name and tag |
| `docker build -f MyDockerfile .` | Custom Dockerfile |
| `docker build --no-cache .` | Ignore cache |
| `docker build --build-arg K=V .` | Pass build argument |
| `docker build --target <stage> .` | Stop at a specific stage |
| `docker build --pull .` | Always pull latest base |
| `docker build --progress plain .` | Full log output |

---

## Volumes

| Command | Description |
|---------|-------------|
| `docker volume create <name>` | Create a named volume |
| `docker volume ls` | List volumes |
| `docker volume inspect <name>` | Details |
| `docker volume rm <name>` | Delete a volume |
| `docker volume prune` | Delete all unused volumes |

---

## Networks

| Command | Description |
|---------|-------------|
| `docker network ls` | List networks |
| `docker network create <name>` | Create a bridge network |
| `docker network inspect <name>` | Details |
| `docker network rm <name>` | Delete a network |
| `docker network prune` | Delete unused networks |
| `docker network connect <net> <ctr>` | Connect container to network |
| `docker network disconnect <net> <ctr>` | Disconnect |

---

## Registry

| Command | Description |
|---------|-------------|
| `docker login` | Log into Docker Hub |
| `docker login <registry>` | Log into a private registry |
| `docker logout` | Log out |
| `docker push <image>` | Push an image |
| `docker pull <image>` | Pull an image |
| `docker search <term>` | Search Docker Hub |

---

## Docker Compose

| Command | Description |
|---------|-------------|
| `docker compose up` | Start all services |
| `docker compose up -d` | Start in background |
| `docker compose up --build` | Rebuild then start |
| `docker compose up --scale svc=3` | Run multiple replicas |
| `docker compose down` | Stop and remove containers + networks |
| `docker compose down -v` | Also remove volumes |
| `docker compose ps` | Status of services |
| `docker compose logs` | All logs |
| `docker compose logs -f <svc>` | Follow one service's logs |
| `docker compose exec <svc> bash` | Shell into a service |
| `docker compose run --rm <svc> <cmd>` | One-off command |
| `docker compose build` | Build images |
| `docker compose pull` | Pull latest images |
| `docker compose restart <svc>` | Restart a service |
| `docker compose stop` | Stop without removing |
| `docker compose start` | Start stopped services |
| `docker compose config` | Validate and print config |

---

## Cleanup

| Command | Description |
|---------|-------------|
| `docker container prune` | Remove stopped containers |
| `docker image prune` | Remove dangling images |
| `docker image prune -a` | Remove all unused images |
| `docker volume prune` | Remove unused volumes |
| `docker network prune` | Remove unused networks |
| `docker builder prune` | Remove build cache |
| `docker system prune` | Remove all unused resources |
| `docker system prune -a --volumes` | Remove absolutely everything unused |
| `docker system df` | Disk usage breakdown |

---

## Dockerfile instructions

| Instruction | Description |
|-------------|-------------|
| `FROM <image>` | Base image (required, first instruction) |
| `RUN <cmd>` | Execute a command and create a layer |
| `COPY <src> <dst>` | Copy files from build context |
| `ADD <src> <dst>` | Like COPY but also extracts archives and fetches URLs |
| `WORKDIR <path>` | Set working directory |
| `ENV <key>=<value>` | Set environment variable (persists at runtime) |
| `ARG <name>` | Build-time variable (not available at runtime) |
| `EXPOSE <port>` | Document the port the app listens on |
| `VOLUME <path>` | Declare a mount point |
| `ENTRYPOINT <cmd>` | Fixed executable, not overridable at `docker run` |
| `CMD <cmd>` | Default command or args (overridable at `docker run`) |
| `LABEL <key>=<value>` | Add metadata |
| `USER <user>` | Set the user for subsequent instructions |
| `HEALTHCHECK` | Define a health check command |
| `ONBUILD <instruction>` | Trigger instruction when image is used as a base |
| `STOPSIGNAL <signal>` | Signal used to stop the container |

---

## Useful one-liners

| Command | Description |
|---------|-------------|
| `docker run --rm -it --entrypoint bash <image>` | Shell into any image |
| `docker rm -f $(docker ps -aq)` | Delete all containers |
| `docker rmi $(docker images -q)` | Delete all images |
| `docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <ctr>` | Get container IP |
| `docker stats --no-stream` | One-shot resource snapshot |
| `docker events` | Stream Docker daemon events |
