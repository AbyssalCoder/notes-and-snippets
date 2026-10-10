## UDP — User Datagram Protocol

- **Connectionless** — no handshake
- **Unreliable** — no delivery guarantee
- **Fast** — minimal overhead

### Use cases
- Video streaming
- Online gaming
- DNS queries
- VoIP

### TCP vs UDP
| Feature      | TCP          | UDP          |
|-------------|-------------|-------------|
| Connection   | Yes          | No           |
| Reliability  | Guaranteed   | Best effort  |
| Speed        | Slower       | Faster       |
| Ordering     | Yes          | No           |


<!-- snippet correction -->

## TCP Three-Way Handshake

1. **SYN** — Client sends SYN with initial sequence number
2. **SYN-ACK** — Server responds with its own SYN + ACK
3. **ACK** — Client acknowledges, connection established

### Why three steps?
Both sides must agree on initial sequence numbers to guarantee reliable, ordered delivery.

### Connection teardown (4-way)
FIN → ACK → FIN → ACK

TCP is **connection-oriented** and **reliable** — it retransmits lost segments.


<!-- snippet correction -->

## DNS Resolution

DNS translates domain names to IP addresses.

### Resolution flow
1. Browser cache → OS cache → Router cache
2. Recursive resolver (ISP)
3. Root nameserver → TLD nameserver → Authoritative nameserver

### Common record types
| Type  | Purpose              | Example            |
|-------|----------------------|--------------------|
| A     | IPv4 address         | 93.184.216.34      |
| AAAA  | IPv6 address         | 2606:2800:220:1::  |
| CNAME | Alias                | www → example.com  |
| MX    | Mail server          | mail.example.com   |
| TXT   | Verification/SPF     | v=spf1 ...         |

```bash
nslookup example.com
dig example.com A
```

## Caching Strategies

### Where to cache
- Browser cache (Cache-Control headers)
- CDN (edge caching)
- Application cache (Redis, Memcached)
- Database query cache

### Cache invalidation strategies
- **TTL** — expire after time
- **Write-through** — update cache on write
- **Write-behind** — async cache update
- **Cache-aside** — app manages cache explicitly

> "There are only two hard things in CS: cache invalidation and naming things."

## Load Balancers

Distribute incoming traffic across multiple servers.

### Algorithms
- **Round Robin** — rotate through servers
- **Least Connections** — send to least busy
- **IP Hash** — consistent routing by client IP
- **Weighted** — proportional to server capacity

### Layer 4 vs Layer 7
- L4: routes based on IP/port (faster)
- L7: routes based on HTTP content (smarter)

Tools: Nginx, HAProxy, AWS ALB/NLB
