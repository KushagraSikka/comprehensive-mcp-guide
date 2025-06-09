# 🔒 MCP Security Best Practices

Securing an MCP deployment involves authentication, authorization, and preventing abuse. This page summarizes recommended patterns.

## OAuth Patterns
MCP servers commonly rely on OAuth 2.0 or OpenID Connect for authentication. A typical flow is:
```text
Client -> Authorization Server -> Token -> MCP Server
```
Use the Authorization Code flow with PKCE for public clients. Tokens should be verified before processing requests.

Example Express middleware:
```javascript
const { verifyToken } = require('./auth');

app.use(async (req, res, next) => {
  try {
    req.user = await verifyToken(req.headers.authorization);
    next();
  } catch (err) {
    res.status(401).send('unauthorized');
  }
});
```
Full server examples are available in [Building MCP Servers](building-servers.md).

## Rate Limiting
To mitigate brute force attacks and runaway clients, enable rate limits:
```javascript
const rateLimit = require('express-rate-limit');
app.use(rateLimit({ windowMs: 60_000, max: 60 }));
```
This restricts each client to 60 requests per minute.

## Additional Tips
- Always serve traffic over HTTPS.
- Validate JSON-RPC payloads against a schema.
- Log authentication events and monitor for anomalies.
- Rotate secrets and credentials regularly.

More deployment tips can be found in the [Production guide](production.md) and general [Best Practices](best-practices.md).
