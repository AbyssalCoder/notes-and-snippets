## 2026-06-04

Explored Pattern Printing — here are my notes.

Understanding the 'why' behind this made everything clearer.

## OSI Model — 7 Layers

| Layer | Name         | Protocol Examples    |
|-------|-------------|---------------------|
| 7     | Application  | HTTP, FTP, SMTP     |
| 6     | Presentation | SSL/TLS, JPEG       |
| 5     | Session      | NetBIOS, RPC        |
| 4     | Transport    | TCP, UDP            |
| 3     | Network      | IP, ICMP            |
| 2     | Data Link    | Ethernet, WiFi      |
| 1     | Physical     | Cables, Signals     |

**Mnemonic:** Please Do Not Throw Sausage Pizza Away (bottom-up)

## Docker Images

Images are read-only templates used to create containers.

### Dockerfile example
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

```bash
docker build -t my-app:1.0 .
docker run -p 8080:8080 my-app:1.0
```

Each instruction creates a layer — order matters for cache efficiency.
