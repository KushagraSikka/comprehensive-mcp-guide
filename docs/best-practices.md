# best-practices Guide

## 📋 Table of Contents
1. [Coding Guidelines](#coding-guidelines)
2. [Deployment Tips](#deployment-tips)
3. [See Also](#see-also)

## Coding Guidelines
Following common patterns keeps MCP services consistent across languages.
Use descriptive method names, validate parameters, and return clear error
responses. Refer to the [Protocol Spec](api-reference/protocol-spec.md) for the
expected JSON-RPC shapes.

## Deployment Tips
When running in production you should implement health checks and structured
logging. The [Architecture guide](architecture.md) explains the runtime
components while the [Security guide](security.md) highlights authentication
strategies.

## See Also
- [Production Guide](production.md)
- [Security Best Practices](security.md)
