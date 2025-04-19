## 🐳 **Docker Command Cheatsheet**

### 🔍 **Image & Container Management**

| Command | Description |
|--------|-------------|
| `docker images` | List all local Docker images |
| `docker ps` | List **running** containers |
| `docker ps -a` | List **all** containers (running + stopped) |
| `docker build -t <image-name> .` | Build an image from a Dockerfile in the current directory |
| `docker rmi <image-name>` | Remove an image (must not be used by any container) |

---

### 🚀 **Running Containers**

| Command | Description |
|---------|-------------|
| `docker run -d -p 8000:8000 --name my-backend backend` | Run a container in detached mode with port mapping |
| `docker start <container-name>` | Start an existing (stopped) container |
| `docker stop <container-name>` | Stop a running container |
| `docker restart <container-name>` | Restart a container |

---

### 🛠️ **Debugging & Logs**

| Command | Description |
|---------|-------------|
| `docker logs <container-name>` | Show logs from a container |
| `docker logs -f <container-name>` | Follow (live tail) the container logs |
| `docker exec -it <container-name> bash` | Open an interactive shell inside a running container |
| `docker inspect <container-name>` | Show detailed configuration and info for a container |

---

### 🧹 **Clean-up**

| Command | Description |
|---------|-------------|
| `docker rm <container-name>` | Remove a **stopped** container |
| `docker rm -f <container-name>` | Force remove a **running** container |
| `docker system prune` | Remove all unused containers, networks, images (⚠️ be careful) |
| `docker volume ls` | List volumes |
| `docker volume rm <volume-name>` | Remove a volume |

---

### 📦 **Volumes & Persistence (Dev)**

| Command | Description |
|---------|-------------|
| `-v $(pwd)/app:/app` | Mount current host directory into the container |
| `-v /app/node_modules` | Ignore mounting node_modules from host to avoid conflicts |