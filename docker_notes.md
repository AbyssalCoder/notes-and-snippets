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
