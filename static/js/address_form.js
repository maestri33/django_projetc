document.addEventListener('DOMContentLoaded', function() {
    const cepInput = document.querySelector('.cep-input');
    const stateSelect = document.querySelector('select[name="state"]');
    const citySelect = document.querySelector('select[name="city"]');
    const birthStateSelect = document.querySelector('select[name="birth_state"]');
    const birthCitySelect = document.querySelector('select[name="birth_city"]');

    function updateCitySelect(stateSelect, citySelect) {
        const state = stateSelect.value;
        citySelect.innerHTML = '<option value="">Selecione uma cidade</option>';
        if (state) {
            fetch(`/api/get_cities_by_state/${state}/`)
                .then(response => response.json())
                .then(data => {
                    data.forEach(([id, name]) => {
                        const option = document.createElement('option');
                        option.value = id;
                        option.textContent = name;
                        citySelect.appendChild(option);
                    });
                });
        }
    }

    if (cepInput) {
        cepInput.addEventListener('blur', function() {
            const cep = this.value.replace(/\D/g, '');
            if (cep.length === 8) {
                fetch(`/api/get_address_from_cep/${cep}/`)
                    .then(response => response.json())
                    .then(data => {
                        if (!data.error) {
                            document.querySelector('input[name="street"]').value = data.street;
                            document.querySelector('input[name="neighborhood"]').value = data.neighborhood;
                            document.querySelector('select[name="state"]').value = data.state;
                            updateCitySelect(stateSelect, citySelect);
                            setTimeout(() => {
                                document.querySelector('select[name="city"]').value = data.city;
                            }, 500);  // Delay to allow city options to populate
                        }
                    });
            }
        });
    }

    if (stateSelect && citySelect) {
        stateSelect.addEventListener('change', () => updateCitySelect(stateSelect, citySelect));
    }

    if (birthStateSelect && birthCitySelect) {
        birthStateSelect.addEventListener('change', () => updateCitySelect(birthStateSelect, birthCitySelect));
    }
});