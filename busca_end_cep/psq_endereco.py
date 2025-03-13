from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def buscar_endereco(localizacao):
    """
    Busca um endereço a partir de um nome de local ou coordenadas geográficas.
    :param localizacao: Nome do local ou coordenadas (latitude, longitude)
    :return: Endereço formatado ou mensagem de erro
    """
    geolocator = Nominatim(user_agent="geoapi")
    
    try:
        location = geolocator.geocode(localizacao, timeout=10)
        if location:
            return f"Endereço encontrado: {location.address}"
        else:
            return "Endereço não encontrado. Verifique a entrada."
    except GeocoderTimedOut:
        return "O serviço de geolocalização demorou muito para responder. Tente novamente."

if __name__ == "__main__":
    entrada = input("Digite o nome do local ou as coordenadas (latitude, longitude): ")
    resultado = buscar_endereco(entrada)
    print(resultado)