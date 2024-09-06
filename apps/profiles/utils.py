import requests
from django.core.cache import cache
from typing import List, Tuple, Optional, Dict

BASE_URL = "https://servicodados.ibge.gov.br/api/v1/localidades"

def get_states() -> List[Tuple[str, str]]:
    """
    Busca a lista de estados brasileiros usando a API do IBGE.
    Retorna uma lista de tuplas (sigla, nome) dos estados.
    """
    cache_key = "ibge_states"
    states = cache.get(cache_key)
    
    if states is None:
        url = f"{BASE_URL}/estados"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            states = [(state["sigla"], state["nome"]) for state in data]
            states.sort(key=lambda x: x[1])  # Ordena os estados alfabeticamente pelo nome
            cache.set(cache_key, states, timeout=86400)  # Cache por 24 horas
        else:
            states = []
    
    return states

def get_cities_by_state(state_uf: str) -> List[Tuple[int, str]]:
    """
    Busca as cidades de um estado usando a API do IBGE.
    Retorna uma lista de tuplas (id, nome) das cidades.
    """
    cache_key = f"ibge_cities_{state_uf}"
    cities = cache.get(cache_key)
    
    if cities is None:
        url = f"{BASE_URL}/estados/{state_uf}/municipios"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            cities = [(city["id"], city["nome"]) for city in data]
            cities.sort(key=lambda x: x[1])  # Ordena as cidades alfabeticamente pelo nome
            cache.set(cache_key, cities, timeout=86400)  # Cache por 24 horas
        else:
            cities = []
    
    return cities

def get_address_from_cep(cep: str) -> Optional[Dict[str, str]]:
    """
    Busca o endereço correspondente a um CEP usando a API ViaCEP.
    """
    cep = cep.replace("-", "").replace(".", "").strip()
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            return {
                "street": data.get("logradouro", ""),
                "neighborhood": data.get("bairro", ""),
                "city": data.get("localidade", ""),
                "state": data.get("uf", ""),
                "zip_code": data.get("cep", "").replace("-", ""),
            }
    return None

def get_regions() -> List[Tuple[int, str]]:
    """
    Busca a lista de regiões brasileiras usando a API do IBGE.
    Retorna uma lista de tuplas (id, nome) das regiões.
    """
    cache_key = "ibge_regions"
    regions = cache.get(cache_key)
    
    if regions is None:
        url = f"{BASE_URL}/regioes"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            regions = [(region["id"], region["nome"]) for region in data]
            cache.set(cache_key, regions, timeout=86400)  # Cache por 24 horas
        else:
            regions = []
    
    return regions