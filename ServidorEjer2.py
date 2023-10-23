import http.server
import socketserver
import json
import random

# Datos ficticios (clima, pais, lista de rep) para países de América Latina
datos_paises={
    "Argentina":{
        "poblacion": random.uniform(40000000, 46000000),
        "temperatura":random.uniform(5, 30),
    "lista_rep":[{"nombre":"Top30Arg", "autor":"Pacific Spain\n","oyentes":random.uniform(0, 100000)}]
    },

    "Brazil":{
        "poblacion": random.uniform(213000000 , 216000000),
        "temperatura":random.uniform(20, 40),
        "lista_rep":[{"nombre":"SambaBrazilia", "autor":"RXDVILL","oyentes":random.uniform(0, 100000)}]
    },

    "Chile":{
        "poblacion": random.uniform(18000000, 20000000),
        "temperatura":random.uniform(5, 25),
        "lista_rep":[{"nombre":"Top 50", "autor":"Spotify","oyentes":random.uniform(0, 10000)}]
    },

    "Colombia":{
        "poblacion": random.uniform(50000000, 52000000),
        "temperatura":random.uniform(20, 35),
        "lista_rep":[{"nombre":"Made in Colombia", "autor":"Spotify","oyentes":random.uniform(0, 10000)}]
    },

    "Mexico":{
        "poblacion": random.uniform(125000000, 127000000),
        "temperatura":random.uniform(10, 30),
        "lista_rep":[{"nombre":"MexicoMX", "autor":"Natalia Cortes","oyentes":random.uniform(0, 10000)}]
    },
}

# Clase personalizada para manejar las solicitudes
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.startswith('/datos/'):
            pais = self.path[7:]
            if pais in datos_paises:
                data = {"datos": datos_paises[pais]}
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
