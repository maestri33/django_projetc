from django.urls import path
from . import views

urlpatterns = [
    # ... outras URLs ...
    path('api/get_address_from_cep/<str:cep>/', views.get_address_from_cep_view, name='get_address_from_cep'),
    path('api/get_cities_by_state/<str:state_uf>/', views.get_cities_by_state_view, name='get_cities_by_state'),
    path('api/get_states/', views.get_states_view, name='get_states'),
    path('api/get_regions/', views.get_regions_view, name='get_regions'),
]