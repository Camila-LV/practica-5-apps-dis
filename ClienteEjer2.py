import requests

##["Argentina", "Brazil", "Chile", "Colombia", "Mexico"]

# Solicitar al usuario que introduzca el nombre del lugar
lugar = input("Introduce el nombre del lugar: ")

# URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9090'

def obtener_informacion(lugar):
    url = f'{url_base}/datos/{lugar}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'Información de {lugar}: {data["datos"]}'
    elif response.status_code == 404:
        return f'Lugar no encontrado: {lugar}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

# Llamar a la función para obtener información sobre el lugar introducido por el usuario
resultado = obtener_informacion(lugar)
print(resultado)
