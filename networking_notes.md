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
