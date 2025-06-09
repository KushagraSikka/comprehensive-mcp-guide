import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import java.io.*;
import java.net.InetSocketAddress;
import java.nio.charset.StandardCharsets;
import java.util.regex.*;

// Basic MCP server in Java.
// Refer to docs/architecture.md for protocol details.
public class Server {
    public static void main(String[] args) throws Exception {
        HttpServer server = HttpServer.create(new InetSocketAddress(8000), 0);
        server.createContext("/rpc", new RpcHandler());
        server.start();
        System.out.println("Java MCP server listening on http://0.0.0.0:8000/rpc");
    }

    static class RpcHandler implements HttpHandler {
        private static final Pattern PARAMS = Pattern.compile("\\[(\\d+),\\s*(\\d+)\\]");
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String body = new String(exchange.getRequestBody().readAllBytes(), StandardCharsets.UTF_8);
            Matcher m = PARAMS.matcher(body);
            int result = 0;
            if (m.find()) {
                int a = Integer.parseInt(m.group(1));
                int b = Integer.parseInt(m.group(2));
                result = a + b;
            }
            String response = "{\"jsonrpc\":\"2.0\",\"result\":" + result + ",\"id\":1}";
            exchange.sendResponseHeaders(200, response.getBytes().length);
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}
