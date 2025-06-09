# ⚡ Performance Optimization Guide

## 📋 Table of Contents
1. [Profiling](#profiling)
2. [Caching](#caching)
3. [See Also](#see-also)

## Profiling
Identify slow methods using standard profilers. For Node.js you can use the
`--inspect` flag or a tool like Clinic.js.

## Caching
Cache expensive operations to reduce response latency:
```javascript
const cache = new Map();
rpc.register('getData', async (id) => {
  if (cache.has(id)) return cache.get(id);
  const data = await db.fetch(id);
  cache.set(id, data);
  return data;
});
```

## See Also
- [Architecture Guide](architecture.md)
