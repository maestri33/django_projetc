from django.contrib import admin
from .models import Profile, Convention, Promoter, EducationalInstitution, ProfileAddress, ConventionAddress

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'birth_date')
    search_fields = ('name', 'email', 'cpf')
    list_filter = ('gender', 'civil_status', 'instruction_level')

@admin.register(Convention)
class ConventionAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'convention_reference')
    search_fields = ('name', 'cnpj', 'convention_reference')

@admin.register(Promoter)
class PromoterAdmin(admin.ModelAdmin):
    list_display = ('profile', 'convention', 'promoter_reference')
    search_fields = ('profile__name', 'convention__name', 'promoter_reference')
    list_filter = ('convention',)

@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'type', 'nature')
    search_fields = ('name', 'cnpj')
    list_filter = ('type', 'nature')

@admin.register(ProfileAddress)
class ProfileAddressAdmin(admin.ModelAdmin):
    list_display = ('profile', 'street', 'city', 'state', 'zip_code')
    search_fields = ('profile__name', 'street', 'city')
    list_filter = ('state', 'type')

@admin.register(ConventionAddress)
class ConventionAddressAdmin(admin.ModelAdmin):
    list_display = ('convention', 'street', 'city', 'state', 'zip_code')
    search_fields = ('convention__name', 'street', 'city')
    list_filter = ('state', 'type')
    
# Register your models here.
