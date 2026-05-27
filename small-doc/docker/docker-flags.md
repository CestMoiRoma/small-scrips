# Docker Flags Reference

All the notable flags, organized by command.

---

## docker run

| Flag | Effect |
|------|--------|
| `-d` / `--detach` | Run in background |
| `-it` | Interactive + allocate a pseudo-TTY (use together for a shell) |
| `--name <name>` | Assign a name to the container |
| `--rm` | Automatically remove the container when it stops |
| `-p <host>:<container>` | Publish a port: `-p 8080:80` |
| `-P` | Publish all exposed ports to random host ports |
| `-e <KEY=value>` | Set an environment variable |
| `--env-file <file>` | Load environment variables from a file |
| `-v <host>:<container>` | Bind mount a host directory |
| `-v <name>:<container>` | Mount a named volume |
| `--mount` | More explicit volume/bind/tmpfs syntax |
| `--network <name>` | Connect to a specific network |
| `--network host` | Use the host network stack |
| `--network none` | Disable all networking |
| `--hostname <name>` | Set the container hostname |
| `--user <uid>:<gid>` | Run as a specific user |
| `--workdir <path>` | Set working directory inside the container |
| `--entrypoint <cmd>` | Override the image's ENTRYPOINT |
| `--memory <size>` | Limit memory (e.g. `512m`, `1g`) |
| `--cpus <n>` | Limit CPU cores (e.g. `1.5`) |
| `--cpu-shares <n>` | Relative CPU weight (default 1024) |
| `--pids-limit <n>` | Limit number of processes |
| `--restart <policy>` | `no`, `always`, `on-failure`, `unless-stopped` |
| `--read-only` | Mount root filesystem as read-only |
| `--privileged` | Give extended privileges (full host access) |
| `--cap-add <cap>` | Add a Linux capability |
| `--cap-drop <cap>` | Drop a Linux capability |
| `--label <key=value>` | Add metadata to the container |
| `--log-driver <name>` | Logging driver: `json-file`, `syslog`, `none`… |
| `--health-cmd <cmd>` | Override healthcheck command |
| `--no-healthcheck` | Disable healthcheck |
| `--init` | Use an init process as PID 1 (handles signals properly) |

---

## docker build

| Flag | Effect |
|------|--------|
| `-t <name:tag>` | Name and optionally tag the image |
| `-f <Dockerfile>` | Specify a custom Dockerfile path |
| `--no-cache` | Build without using any cached layers |
| `--build-arg <KEY=value>` | Pass a build-time variable |
| `--target <stage>` | Stop at a specific stage (multi-stage builds) |
| `--platform <platform>` | Target platform: `linux/amd64`, `linux/arm64` |
| `--pull` | Always pull a newer base image |
| `--progress plain` | Show full build output (no fancy progress) |
| `--squash` | Squash all layers into one (experimental) |
| `--label <key=value>` | Add metadata to the image |
| `--secret id=<id>,src=<file>` | Mount a secret at build time (not stored in layer) |
| `--ssh default` | Forward SSH agent to the build |
| `--output type=local,dest=.` | Export build output to the local filesystem |

---

## docker ps

| Flag | Effect |
|------|--------|
| `-a` / `--all` | Show all containers (default: running only) |
| `-q` / `--quiet` | Only display container IDs |
| `-s` / `--size` | Show container size on disk |
| `-n <n>` | Show last n containers |
| `-f <filter>` | Filter: `-f status=exited`, `-f name=web`, `-f label=env=prod` |
| `--format` | Custom output: `--format "table {{.Names}}\t{{.Status}}"` |
| `--no-trunc` | Don't truncate output |

---

## docker logs

| Flag | Effect |
|------|--------|
| `-f` / `--follow` | Follow log output in real time |
| `--tail <n>` | Show last n lines |
| `--since <time>` | Show logs since timestamp or duration: `--since 1h` |
| `--until <time>` | Show logs before a timestamp |
| `-t` / `--timestamps` | Show timestamps |

---

## docker exec

| Flag | Effect |
|------|--------|
| `-i` / `--interactive` | Keep stdin open |
| `-t` / `--tty` | Allocate a pseudo-TTY |
| `-e <KEY=value>` | Set an environment variable |
| `-u <user>` | Run as a specific user |
| `-w <path>` | Set working directory |
| `-d` / `--detach` | Run in background |

---

## docker images

| Flag | Effect |
|------|--------|
| `-a` / `--all` | Show all images including intermediate layers |
| `-q` / `--quiet` | Only print image IDs |
| `--no-trunc` | Don't truncate image IDs |
| `-f <filter>` | Filter: `-f dangling=true`, `-f label=version=1.0` |
| `--format` | Custom output format |
| `--digests` | Show image digests |

---

## docker network

| Command | Flag | Effect |
|---------|------|--------|
| `create` | `--driver <name>` | Network driver: `bridge`, `overlay`, `host`, `none` |
| `create` | `--subnet <cidr>` | Subnet: `--subnet 172.20.0.0/16` |
| `create` | `--gateway <ip>` | Custom gateway IP |
| `create` | `--internal` | No external connectivity |
| `create` | `--attachable` | Allow manual container attachment (overlay) |
| `ls` | `-f <filter>` | Filter by driver, name, etc. |
| `connect` | `--ip <ip>` | Assign a specific IP to the container |
| `connect` | `--alias <name>` | Add a network-scoped alias |

---

## docker volume

| Command | Flag | Effect |
|---------|------|--------|
| `create` | `--driver <name>` | Volume driver (default: `local`) |
| `create` | `--opt o=uid=1000` | Driver-specific options |
| `ls` | `-f dangling=true` | Show only unused volumes |
| `prune` | `-f` | Skip confirmation prompt |
| `inspect` | `--format` | Custom output format |

---

## docker compose

| Flag | Effect |
|------|--------|
| `-f <file>` | Specify a compose file (default: `compose.yml`) |
| `--project-name <name>` / `-p` | Set project name (default: directory name) |
| `--env-file <file>` | Specify a `.env` file |
| `--profile <name>` | Enable a specific profile |
| `up -d` | Start in detached mode |
| `up --build` | Rebuild images before starting |
| `up --force-recreate` | Recreate containers even if unchanged |
| `up --no-deps` | Don't start linked services |
| `up --scale svc=3` | Run multiple instances of a service |
| `down -v` | Also remove volumes |
| `down --rmi all` | Also remove images |
| `logs --no-log-prefix` | Hide service name prefix in logs |
| `run --rm` | Remove container after one-off run |
| `run --no-deps` | Don't start dependent services |

---

## docker system / prune

| Command | Flag | Effect |
|---------|------|--------|
| `system prune` | `-a` | Also remove unused images (not just dangling) |
| `system prune` | `--volumes` | Also remove unused volumes |
| `system prune` | `-f` | Skip confirmation |
| `system prune` | `--filter <f>` | Only prune matching resources |
| `image prune` | `-a` | Remove all unused images |
| `container prune` | `-f` | Skip confirmation |
| `volume prune` | `-f` | Skip confirmation |
| `builder prune` | `-a` | Remove all build cache |
