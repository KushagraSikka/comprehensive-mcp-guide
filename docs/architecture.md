# 🏗️ MCP Architecture Deep Dive

This section describes how the core components of MCP interact and how JSON-RPC requests flow through the system.

## High Level Diagram
```text
+-----------+        HTTP        +------------+
|   Client  | <---- Requests --> | MCP Server |
+-----------+                    +------------+
        |                              |
        |          JSON-RPC 2.0        |
        +------------------------------+
```
For instructions on running a local server read the [Getting Started guide](getting-started.md).

## Components
- **Client** – Sends JSON-RPC requests to the server.
- **Server** – Receives requests and dispatches them to handlers.
- **Transport** – HTTP is common, but WebSocket or other transports can be used.

## JSON-RPC Flow
1. A client sends a request like the following:
```json
{
  "jsonrpc": "2.0",
  "method": "sum",
  "params": [1, 2],
  "id": 42
}
```
2. The server validates the request.
3. The appropriate handler is executed.
4. The result is encoded back into JSON-RPC format and returned.

Diagram of the request lifecycle:
```text
Client --HTTP POST--> /rpc --Router--> Handler --Result--> Client
```
See the full protocol specification in [JSON-RPC Reference](api-reference/json-rpc.md).

## Related Documents
- [Security Best Practices](security.md)
- [Performance Guide](performance.md)
- [Building MCP Servers](building-servers.md)
