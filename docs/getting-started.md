# 🚀 Getting Started with Model Context Protocol (MCP)

Welcome to the MCP guide. This page shows how to set up the environment and run a simple server.

## 📋 Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Your First MCP Server](#your-first-mcp-server)
4. [Next Steps](#next-steps)

## Introduction
Model Context Protocol (MCP) defines a light-weight JSON-RPC 2.0 interface for model integrations. If you are looking for a detailed overview of the components, check the [Architecture guide](architecture.md). When deploying publicly you should also read the [Security Best Practices](security.md).

## Installation
### Prerequisites
- Node.js 16+
- Git

Clone the repository and install dependencies:
```bash
git clone https://example.com/comprehensive-mcp-guide.git
cd comprehensive-mcp-guide
npm install
```

### Running the Example
Start the example server included in this repository:
```bash
node examples/basic-server.js
```
The server will listen on `http://localhost:4000/rpc`.

## Your First MCP Server
Below is a minimal Node.js implementation using the hypothetical `mcp` module:
```javascript
const express = require('express');
const { createServer } = require('mcp');

const app = express();
app.post('/rpc', createServer());

app.listen(4000, () => {
  console.log('MCP server running on http://localhost:4000/rpc');
});
```
Send a request with `curl`:
```bash
curl -X POST http://localhost:4000/rpc \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"echo","params":["hello"],"id":1}'
```
For additional client APIs see [Client API](api-reference/client-api.md).

## Next Steps
- Explore server development in [Building MCP Servers](building-servers.md).
- Review optimization techniques in the [Performance Guide](performance.md).
- When you're ready for production, read the [Production guide](production.md).
