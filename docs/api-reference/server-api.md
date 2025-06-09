# server-api Reference

## 📋 Table of Contents
1. [Overview](#overview)
2. [Registering Methods](#registering-methods)

## Overview
The server API exposes helpers to register methods and start an HTTP listener.

## Registering Methods
```javascript
import { createServer } from 'mcp';

const server = createServer();
server.register('echo', (msg) => msg);
```

See [Client API](client-api.md) for invoking these methods.
