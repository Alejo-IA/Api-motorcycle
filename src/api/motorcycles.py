import requests
from src.config import API_KEY, BASE_URL

def buscar_motos(marca="", modelo="", anio="", tipo=""):
    """
    Busca motos usando la API de Ninjas
    
    Args:
        marca (str): Marca de la moto
        modelo (str): Modelo de la moto
        anio (str): Año de la moto
        tipo (str): Tipo de moto
        
    Returns:
        list: Lista de motos encontradas
    """
    # Construcción de parámetros
    parametros = {}
    if marca:
        parametros["make"] = marca
    if modelo:
        parametros["model"] = modelo
    if anio:
        parametros["year"] = anio
    if tipo and tipo.lower() != "todos":
        parametros["type"] = tipo.lower()
    
    headers = {"X-Api-Key": API_KEY}
    
    try:
        response = requests.get(BASE_URL, headers=headers, params=parametros)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error al comunicarse con la API: {e}")