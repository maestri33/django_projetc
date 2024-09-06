from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .utils import get_address_from_cep, get_cities_by_state, get_states, get_regions

@require_GET
def get_address_from_cep_view(request, cep):
    address_data = get_address_from_cep(cep)
    if address_data:
        return JsonResponse(address_data)
    return JsonResponse({"error": "CEP não encontrado"}, status=404)

@require_GET
def get_cities_by_state_view(request, state_uf):
    cities = get_cities_by_state(state_uf)
    return JsonResponse(cities, safe=False)

@require_GET
def get_states_view(request):
    states = get_states()
    return JsonResponse(states, safe=False)

@require_GET
def get_regions_view(request):
    regions = get_regions()
    return JsonResponse(regions, safe=False)