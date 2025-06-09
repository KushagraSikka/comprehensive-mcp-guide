# protocol-spec Reference

## 📋 Table of Contents
1. [Envelope](#envelope)
2. [Batching](#batching)

## Envelope
Every JSON-RPC message MUST include the fields `jsonrpc`, `method`, `id`, and
optionally `params` and `result`/`error`.

## Batching
Multiple requests can be sent in a single HTTP call by sending an array of
objects. Responses will be returned in the same order.

The protocol is implemented by the server described in the
[Architecture guide](../architecture.md).
