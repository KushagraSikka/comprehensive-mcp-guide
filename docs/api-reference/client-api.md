# client-api Reference

## 📋 Table of Contents
1. [Overview](#overview)
2. [Example Request](#example-request)
3. [See Also](#see-also)

## Overview
The client library simplifies sending JSON-RPC requests to MCP servers.
It automatically handles batching and error formatting.

## Example Request
```javascript
import { Client } from 'mcp';
const client = new Client('http://localhost:4000/rpc');
const result = await client.call('sum', [1, 2]);
```

## See Also
- [Server API](server-api.md)
- [Security Best Practices](../security.md)
