# transport-layer Reference

## 📋 Table of Contents
1. [HTTP](#http)
2. [WebSocket](#websocket)

## HTTP
Most deployments rely on HTTP POST for transporting JSON-RPC messages. Ensure
TLS is enabled as recommended in [Security Best Practices](../security.md).

## WebSocket
For bidirectional scenarios you can use WebSocket. The protocol framing remains
the same; only the transport changes. Consult the [Architecture guide](../architecture.md)
for details on how the server handles different transports.
