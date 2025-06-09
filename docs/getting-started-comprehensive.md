# 🚀 Getting Started with Model Context Protocol (MCP)

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Running the Demo](#running-the-demo)
3. [Next Steps](#next-steps)

## Prerequisites
Install Node.js 16+ and clone this repository. Details about the system design
are available in the [Architecture guide](architecture.md).

## Running the Demo
Install dependencies and start the sample server:

```bash
npm install
node examples/basic-server.js
```

Send a request:
```bash
curl -X POST http://localhost:4000/rpc \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"echo","params":["hi"],"id":1}'
```

## Next Steps
- Read about deployment in [Production](production.md).
- Review [Security Best Practices](security.md) before exposing your server.
