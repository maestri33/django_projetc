from django import forms
from .models import Profile, AbstractAddress
from .utils import get_cities_by_state, get_states, get_address_from_cep

class ProfileForm(forms.ModelForm):
    birth_state = forms.ChoiceField(choices=[], label="Estado de Nascimento")
    birth_city = forms.ChoiceField(choices=[], label="Cidade de Nascimento")

    class Meta:
        model = Profile
        fields = ['birth_state', 'birth_city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['birth_state'].choices = [("", "Selecione um estado")] + get_states()
        self.fields['birth_city'].choices = [("", "Selecione uma cidade")]

    def clean(self):
        cleaned_data = super().clean()
        birth_state = cleaned_data.get('birth_state')
        birth_city = cleaned_data.get('birth_city')

        if birth_state:
            cities = get_cities_by_state(birth_state)
            self.fields['birth_city'].choices = [("", "Selecione uma cidade")] + cities

        if birth_city and int(birth_city) not in [int(choice[0]) for choice in self.fields['birth_city'].choices if choice[0]]:
            self.add_error('birth_city', 'Cidade inválida para o estado selecionado.')

        return cleaned_data

class AddressForm(forms.ModelForm):
    state = forms.ChoiceField(choices=[], label="Estado")
    city = forms.ChoiceField(choices=[], label="Cidade")

    class Meta:
        model = AbstractAddress
        fields = ['street', 'number', 'complement', 'neighborhood', 'city', 'state', 'zip_code', 'type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['zip_code'].widget.attrs.update({'class': 'cep-input'})
        self.fields['state'].choices = [("", "Selecione um estado")] + get_states()
        self.fields['city'].choices = [("", "Selecione uma cidade")]

    def clean_zip_code(self):
        zip_code = self.cleaned_data.get('zip_code')
        if zip_code:
            address_data = get_address_from_cep(zip_code)
            if address_data:
                for field, value in address_data.items():
                    if field in self.fields:
                        self.cleaned_data[field] = value
            else:
                raise forms.ValidationError("CEP inválido ou não encontrado.")
        return zip_code

    def clean(self):
        cleaned_data = super().clean()
        state = cleaned_data.get('state')
        city = cleaned_data.get('city')

        if state:
            cities = get_cities_by_state(state)
            self.fields['city'].choices = [("", "Selecione uma cidade")] + cities

        if city and int(city) not in [int(choice[0]) for choice in self.fields['city'].choices if choice[0]]:
            self.add_error('city', 'Cidade inválida para o estado selecionado.')

        return cleaned_data