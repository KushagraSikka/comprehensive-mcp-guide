# advanced-features Guide

## 📋 Table of Contents
1. [Overview](#overview)
2. [Request Hooks](#request-hooks)
3. [Streaming Responses](#streaming-responses)
4. [See Also](#see-also)

## Overview
This page explores optional capabilities that go beyond the basic MCP workflow.
These features build upon the concepts introduced in the
[Architecture guide](architecture.md) and should be secured as described in the
[Security Best Practices](security.md).

## Request Hooks
Handlers can register middleware that executes before or after JSON-RPC methods
run. Below is a small example using the fictional `mcp` module:

```javascript
const { createServer } = require('mcp');

function logRequest(ctx, next) {
  console.log('method:', ctx.method);
  return next();
}

const server = createServer({ hooks: [logRequest] });
```

## Streaming Responses
Some implementations support streaming large responses back to the client.
Instead of returning the full payload, the server yields chunks asynchronously:

```javascript
async function* streamData() {
  yield 'part 1';
  yield 'part 2';
}

rpc.register('streamExample', async () => streamData());
```

## See Also
- [Architecture Guide](architecture.md)
- [Security Best Practices](security.md)
