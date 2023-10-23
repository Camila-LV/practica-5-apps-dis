import http.server
import socketserver
import json
import random

# Datos ficticios de temperatura para países de América Latina
personas = {
    "Argentina": 4604470,
    "Brazil": 203062512,
    "Chile": random.uniform(17574003, 19960889),
    "Colombia": 52156254,
    "Mexico": random.uniform(126014024, 129875529),
}
temperaturas = {
    "Argentina": random.uniform(5, 30),
    "Brazil": random.uniform(20, 40),
    "Chile": random.uniform(5, 25),
    "Colombia": random.uniform(20, 35),
    "Mexico": random.uniform(10, 30),
}
playlist = {
    "Argentina": [{"nombre":"Top30Arg", "autor":"Pacific Spain\n","oyentes":random.uniform(85000, 100000)}],
    "Brazil": [{"nombre":"SambaBrazilia", "autor":"RXDVILL","oyentes":random.uniform(85000, 100000)}],
    "Chile": [{"nombre":"Top 50", "autor":"Spotify","oyentes":random.uniform(85000, 10000)}],
    "Colombia": [{"nombre":"Made in Colombia", "autor":"Spotify","oyentes":random.uniform(85000, 10000)}],
    "Mexico": [{"nombre":"MexicoMX", "autor":"Natalia Cortes","oyentes":random.uniform(85000, 10000)}],
}

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/temperature/'):
            pais = self.path[13:]
            if pais in temperaturas:
                data = {"temperature": temperaturas[pais]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())  # Codificar la cadena a bytes ya que desconoces tu Cliente
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())  # Codificar la cadena a bytes
        elif self.path.startswith('/population/'):
            pais = self.path[12:]
            if pais in personas:
                data = {"population": personas[pais]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())  # Codificar la cadena a bytes
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())  # Codificar la cadena a bytes
        elif self.path.startswith('/music/'):
            pais = self.path[7:]
            if pais in playlist:
                data = {"playlist": playlist[pais]}
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())  # Codificar la cadena a bytes
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("País no encontrado.".encode())  # Codificar la cadena a bytes
        else:
            super().do_GET()

# Configuración del servidor
with socketserver.TCPServer(("", 9090), MyHandler) as httpd:
    print("Servidor web en el puerto 9090")
    httpd.serve_forever()
