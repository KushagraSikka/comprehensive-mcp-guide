# json-rpc Reference

## 📋 Table of Contents
1. [Overview](#overview)
2. [Request Example](#request-example)

## Overview
MCP is based on the JSON-RPC 2.0 specification. Each request is a JSON object
containing a `method`, optional `params`, and an `id`.

## Request Example
```json
{
  "jsonrpc": "2.0",
  "method": "echo",
  "params": ["hello"],
  "id": 1
}
```

See [Protocol Spec](protocol-spec.md) for the full wire format.
