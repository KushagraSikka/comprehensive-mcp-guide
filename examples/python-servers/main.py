"""Async MCP server example.
Refer to docs/architecture.md for JSON-RPC flow.
"""
import asyncio
import json

async def handle(reader, writer):
    data = await reader.read(1024)
    request = json.loads(data.decode())
    result = sum(request.get("params", [])) if request.get("method") == "sum" else None
    response = {"jsonrpc": "2.0", "result": result, "id": request.get("id")}
    writer.write(json.dumps(response).encode())
    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle, "0.0.0.0", 8001)
    print("Async MCP server running on port 8001")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
