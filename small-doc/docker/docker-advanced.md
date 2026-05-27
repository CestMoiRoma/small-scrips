# Docker Advanced

---

## Docker Compose

Define and run multi-container applications with a `compose.yml` file.

```yaml
# compose.yml
services:
  app:
    build: .                          # build from local Dockerfile
    ports:
      - "8080:80"
    environment:
      - DB_HOST=db
      - DB_PORT=5432
    env_file:
      - .env                          # load variables from a file
    volumes:
      - ./src:/app/src                # bind mount
      - uploads:/app/uploads          # named volume
    depends_on:
      db:
        condition: service_healthy    # wait for healthcheck
    restart: unless-stopped
    networks:
      - backend

  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "postgres"]
      interval: 5s
      timeout: 3s
      retries: 5
    networks:
      - backend

volumes:
  pgdata:
  uploads:

networks:
  backend:
```

```bash
docker compose up               # start all services (foreground)
docker compose up -d            # detached
docker compose up --build       # rebuild images before starting
docker compose down             # stop and remove containers + networks
docker compose down -v          # also remove volumes
docker compose ps               # status of services
docker compose logs             # all logs
docker compose logs -f app      # follow logs for a specific service
docker compose exec app bash    # shell into a running service
docker compose run app python manage.py migrate  # one-off command
docker compose build            # build images without starting
docker compose pull             # pull latest images
docker compose restart app      # restart one service
docker compose stop             # stop without removing
docker compose start            # start stopped services
docker compose config           # validate and print resolved config
```

---

## Multi-stage builds

Reduce final image size by separating build dependencies from runtime.

```dockerfile
# ── Stage 1: build ────────────────────────────────────────────
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# ── Stage 2: runtime ──────────────────────────────────────────
FROM nginx:alpine AS runtime
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

```bash
docker build --target builder .      # build only up to a specific stage
```

---

## Build arguments vs environment variables

| | `ARG` | `ENV` |
|-|-------|-------|
| Available at | Build time only | Build time + runtime |
| Visible in `docker inspect` | No | Yes |
| Override at runtime | No | Yes (`-e`) |
| Use case | Build-time config, versions | App config |

```dockerfile
ARG NODE_VERSION=20
FROM node:${NODE_VERSION}

ARG BUILD_DATE
LABEL build-date=$BUILD_DATE

ENV APP_ENV=production
```

```bash
docker build --build-arg NODE_VERSION=18 .
```

---

## Healthchecks

```dockerfile
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1
```

```bash
docker inspect --format='{{.State.Health.Status}}' <container>
```

States: `starting` → `healthy` / `unhealthy`

---

## Resource limits

```bash
docker run --memory="512m" <image>          # max memory
docker run --memory-swap="1g" <image>       # max memory + swap
docker run --cpus="1.5" <image>             # max CPU cores
docker run --cpu-shares=512 <image>         # relative CPU weight (default 1024)
docker run --pids-limit=100 <image>         # max processes
```

In Compose:
```yaml
services:
  app:
    deploy:
      resources:
        limits:
          cpus: "1.5"
          memory: 512M
```

---

## Registry & pushing images

```bash
docker login                               # log into Docker Hub
docker login registry.example.com         # log into a private registry

docker tag myapp:1.0 username/myapp:1.0   # tag for Docker Hub
docker push username/myapp:1.0            # push to Docker Hub

docker tag myapp:1.0 registry.example.com/myapp:1.0
docker push registry.example.com/myapp:1.0

docker pull registry.example.com/myapp:1.0
docker logout
```

---

## Docker Buildx (multi-platform)

Build images for multiple architectures (e.g., amd64 + arm64).

```bash
docker buildx create --use --name mybuilder    # create a builder
docker buildx inspect --bootstrap              # verify it's ready

docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t username/myapp:1.0 \
  --push .                                     # build and push directly
```

---

## Networking deep dive

| Driver | Use case |
|--------|----------|
| `bridge` | Default. Isolated network on a single host. Containers talk by name on custom bridges. |
| `host` | Container shares the host's network stack. No isolation, best performance. |
| `none` | No networking at all. |
| `overlay` | Multi-host networking. Used with Docker Swarm. |
| `macvlan` | Assign a MAC address to the container — appears as a physical device on the network. |

```bash
# Custom bridge — containers resolve each other by name
docker network create --driver bridge mynet
docker run --network mynet --name api <image>
docker run --network mynet --name web <image>
# web can reach api at http://api:<port>

# Host network
docker run --network host <image>
```

---

## Secrets & sensitive data

Never put secrets in environment variables or `ARG` — they end up in image history.

**With Docker Compose:**
```yaml
services:
  app:
    secrets:
      - db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```
Secret is mounted at `/run/secrets/db_password` inside the container.

**At runtime (tmpfs):**
```bash
docker run --mount type=tmpfs,destination=/secrets <image>
```

---

## Useful patterns

```bash
# Get a shell in a stopped container
docker run --rm -it --entrypoint bash <image>

# Override the entrypoint
docker run --entrypoint "" <image> sh

# Run as a specific user
docker run --user 1000:1000 <image>

# Mount Docker socket (for Docker-in-Docker or CI)
docker run -v /var/run/docker.sock:/var/run/docker.sock <image>

# Inspect container IP
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container>

# Follow logs since a timestamp
docker logs --since 2024-01-01T00:00:00 -f <container>

# Export / import a container as a tar
docker export <container> > backup.tar
docker import backup.tar myimage:restored

# Save / load an image as a tar (preserves layers)
docker save myimage:1.0 | gzip > myimage.tar.gz
docker load < myimage.tar.gz
```
