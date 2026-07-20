## Git Branching

```bash
git branch feature-x            # Create branch
git checkout feature-x           # Switch to branch
git checkout -b feature-y        # Create + switch
git branch -d feature-x          # Delete branch
git merge feature-y              # Merge into current
```

### Best practices
- Keep branches short-lived
- Use descriptive names: `feature/login`, `fix/header-bug`
- Delete merged branches

## Docker Basics

Docker packages applications into containers — lightweight, portable units.

### Key commands
```bash
docker run hello-world              # Run a test container
docker ps                            # List running containers
docker ps -a                         # List all containers
docker images                        # List local images
docker stop <container_id>           # Stop a container
docker rm <container_id>             # Remove a container
docker rmi <image_id>                # Remove an image
```

**Container ≠ VM** — containers share the host kernel.

## Nginx Basics

Nginx is a high-performance web server and reverse proxy.

### Basic config
```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        root /var/www/html;
        index index.html;
    }

    location /api {
        proxy_pass http://localhost:3000;
    }
}
```

```bash
sudo nginx -t           # Test config
sudo systemctl reload nginx  # Reload
```

## Docker Volumes

Volumes persist data beyond container lifecycle.

```bash
# Named volume
docker volume create mydata
docker run -v mydata:/app/data nginx

# Bind mount (host directory)
docker run -v $(pwd)/data:/app/data nginx

# List volumes
docker volume ls

# Inspect
docker volume inspect mydata
```

Prefer named volumes over bind mounts in production.
