import requests

# URL del servidor web (asegúrate de que la dirección y el puerto coincidan)
url_base = 'http://localhost:9090'

def obtener_temperatura(pais):
    url = f'{url_base}/temperature/{pais}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'Temperatura en {pais}: {data["temperature"]:.2f}°C'
    elif response.status_code == 404:
        return f'País no encontrado: {pais}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

def obtener_poblacion(pais):
    url = f'{url_base}/population/{pais}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'La población en {pais}: {data["population"]} personas'
    elif response.status_code == 404:
        return f'País no encontrado: {pais}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'

def obtener_musica(pais):
    url = f'{url_base}/music/{pais}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return f'Las listas de reproducción en {pais}: {data["playlist"]} personas'
    elif response.status_code == 404:
        return f'País no encontrado: {pais}'
    else:
        return f'Error en la solicitud: Código {response.status_code}'


# Ejemplos de uso
paises = ["Argentina", "Brazil", "Chile", "Colombia", "Mexico"]
for pais in paises:
    resultado_temperatura = obtener_temperatura(pais)
    print(resultado_temperatura)
    resultado_poblacion = obtener_poblacion(pais)
    print(resultado_poblacion)
    resultado_musica = obtener_musica(pais)
    print(resultado_musica)
