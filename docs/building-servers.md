# Building MCP Servers - Complete development guide with TypeScript, Python, Go, and Rust examples

## 📋 Table of Contents
1. [Overview](#overview)
2. [Example Server](#example-server)
3. [See Also](#see-also)

## Overview
This page demonstrates how to implement an MCP server in various languages. It
assumes familiarity with the components in the
[Architecture guide](architecture.md).

## Example Server
Below is a short TypeScript example using Express:

```typescript
import express from 'express';
import { createServer } from 'mcp';

const app = express();
app.post('/rpc', createServer());

app.listen(4000, () => console.log('MCP server running'));
```

Other languages follow the same pattern—initialize a router and expose a JSON-RPC
endpoint. Secure the route using the recommendations in
[Security Best Practices](security.md).

## See Also
- [Security Best Practices](security.md)
- [Advanced Features](advanced-features.md)
