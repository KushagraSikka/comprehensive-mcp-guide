# enterprise-deployment Guide

## 📋 Table of Contents
1. [Overview](#overview)
2. [High Availability](#high-availability)
3. [See Also](#see-also)

## Overview
Enterprises often deploy MCP at scale with strict uptime and compliance
requirements. A robust architecture is described in the
[Architecture guide](architecture.md).

## High Availability
Use container orchestration (Kubernetes, Docker Swarm) to manage replicas and
perform rolling updates. Secure endpoints using the patterns in
[Security Best Practices](security.md).

```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: 3
  template:
    metadata:
      labels:
        app: mcp
    spec:
      containers:
        - name: mcp
          image: my-mcp:latest
```

## See Also
- [Performance Guide](performance.md)
- [Security Best Practices](security.md)
