import java.io.*;
import java.net.*;
import com.sun.net.httpserver.*;

public class Main {
    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);

        server.createContext("/api/hello", new TestHandler());

        server.setExecutor(null);
        server.start();

        System.out.println("Server is listening on port 8080");
    }

    static class TestHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            if ("GET".equals(exchange.getRequestMethod())) {
                String response = "Hello, World";
                System.out.println(response);
                exchange.sendResponseHeaders(200, response.getBytes().length);
                OutputStream os = exchange.getResponseBody();
                os.write(response.getBytes());
                os.close();
            }
            else {
                exchange.sendResponseHeaders(400, -1);
            }
        }
    }
}