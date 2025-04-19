frontend
docker build -t frontend:latest .
docker run -d -p 3000:3000 --name my-frontend frontend

backend
docker build -t backend:latest .
docker run -d -p 8000:8000 --name my-backend backend


docker images
docker ps
docker ps -a # See all containers, including stopped ones
docker start <containerName>
docker stop <containerName>
docker rm <containerName>
docker logs <containerName>       # see the stdout/stderr of container
docker logs -f <containerName>    # stream watching logs（tail -f）

# 1. Stop and remove existing containers
docker stop my-frontend my-backend
docker rm my-frontend my-backend

# 2. Restart them with proper port bindings
docker run -d --name my-backend -p 8000:8000 --network my-network backend
docker run -d --name my-frontend -p 3000:3000 --network my-network frontend



