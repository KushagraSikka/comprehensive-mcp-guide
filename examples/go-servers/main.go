// Basic MCP server in Go.
// See docs/architecture.md for details on the JSON-RPC flow.
package main

import (
    "encoding/json"
    "net/http"
)

type Request struct {
    JSONRPC string `json:"jsonrpc"`
    Method  string `json:"method"`
    Params  []int  `json:"params"`
    ID      int    `json:"id"`
}

type Response struct {
    JSONRPC string `json:"jsonrpc"`
    Result  int    `json:"result"`
    ID      int    `json:"id"`
}

func rpcHandler(w http.ResponseWriter, r *http.Request) {
    var req Request
    json.NewDecoder(r.Body).Decode(&req)
    res := Response{JSONRPC: "2.0", ID: req.ID}
    if req.Method == "sum" && len(req.Params) >= 2 {
        res.Result = req.Params[0] + req.Params[1]
    }
    json.NewEncoder(w).Encode(res)
}

func main() {
    http.HandleFunc("/rpc", rpcHandler)
    http.ListenAndServe(":8000", nil)
}
