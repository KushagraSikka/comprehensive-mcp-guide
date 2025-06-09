# migration-guide Guide

## 📋 Table of Contents
1. [From Legacy APIs](#from-legacy-apis)
2. [Compatibility Tips](#compatibility-tips)

## From Legacy APIs
When migrating from a REST or GraphQL interface, map existing endpoints to
JSON-RPC methods. The [Protocol Spec](api-reference/protocol-spec.md) explains
the request and response structures.

## Compatibility Tips
Use versioned method names (e.g. `user.create.v2`) to avoid breaking existing
clients. Carefully document changes and follow the security checklist in
[Security Best Practices](security.md).
