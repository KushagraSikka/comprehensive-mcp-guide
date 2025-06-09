use serde::{Deserialize, Serialize};
use tiny_http::{Server, Response};

#[derive(Deserialize)]
struct RpcRequest {
    jsonrpc: String,
    method: String,
    params: Vec<i32>,
    id: i32,
}

#[derive(Serialize)]
struct RpcResponse {
    jsonrpc: String,
    result: i32,
    id: i32,
}

// Basic MCP server in Rust.
// See docs/architecture.md for an overview of the protocol.
fn main() {
    let server = Server::http("0.0.0.0:8000").unwrap();
    println!("Rust MCP server running on http://0.0.0.0:8000");
    for request in server.incoming_requests() {
        let rpc: RpcRequest = serde_json::from_reader(request.as_reader()).unwrap();
        let result = if rpc.method == "sum" { rpc.params.iter().sum() } else { 0 };
        let response = RpcResponse { jsonrpc: "2.0".into(), result, id: rpc.id };
        let body = serde_json::to_string(&response).unwrap();
        let _ = request.respond(Response::from_string(body));
    }
}
