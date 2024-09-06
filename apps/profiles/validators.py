import re
from datetime import date
from django.core.exceptions import ValidationError
from django.utils import timezone

# Constantes para validação
PHONE_NUMBER_LENGTH = 11
CPF_LENGTH = 11

# Mensagens de erro
INVALID_PHONE_NUMBER_MESSAGE = "O número de telefone deve conter {length} dígitos."
INVALID_PHONE_NUMBER_DDD_MESSAGE = "O DDD do telefone é inválido."
PHONE_NUMBER_START_DIGIT = "O número de telefone deve começar com o dígito 9."
INVALID_CPF_MESSAGE = "CPF inválido."
INVALID_BIRTHDATE_MESSAGE = "A data de nascimento não pode ser maior que a data atual."
CEP_NOT_FOUND_ERROR_MESSAGE = "CEP não encontrado. Por favor, verifique e tente novamente."

# Lista de DDDs válidos no Brasil
VALID_DDDS = {
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "21", "22", "24", "27", "28",
    "31", "32", "33", "34", "35", "37", "38", "41", "42", "43", "44", "45", "46", "47",
    "48", "49", "51", "53", "54", "55", "61", "62", "63", "64", "65", "66", "67", "68",
    "69", "71", "73", "74", "75", "77", "79", "81", "82", "83", "84", "85", "86", "87",
    "88", "89", "91", "92", "93", "94", "95", "96", "97", "98", "99"
}

def validate_phone(value):
    """
    Valida e formata um número de telefone brasileiro.
    
    Args:
        value (str): O número de telefone a ser validado.
    
    Returns:
        str: O número de telefone formatado.
    
    Raises:
        ValidationError: Se o número de telefone for inválido.
    """
    phone_number = re.sub(r"\D", "", value)
    if len(phone_number) != PHONE_NUMBER_LENGTH:
        raise ValidationError(
            INVALID_PHONE_NUMBER_MESSAGE.format(length=PHONE_NUMBER_LENGTH),
            code="invalid_phone_number",
        )

    ddd = phone_number[:2]
    if ddd not in VALID_DDDS:
        raise ValidationError(
            INVALID_PHONE_NUMBER_DDD_MESSAGE,
            code="invalid_phone_number",
        )
    if phone_number[2] != "9":
        raise ValidationError(
            PHONE_NUMBER_START_DIGIT,
            code="invalid_phone_number",
        )

    return f"+55 ({ddd}) {phone_number[2:7]}-{phone_number[7:]}"

def validate_cpf(value):
    """
    Valida e formata um CPF brasileiro.
    
    Args:
        value (str): O CPF a ser validado.
    
    Returns:
        str: O CPF formatado.
    
    Raises:
        ValidationError: Se o CPF for inválido.
    """
    cpf = [int(char) for char in value if char.isdigit()]
    if len(cpf) != CPF_LENGTH or len(set(cpf)) == 1:
        raise ValidationError(INVALID_CPF_MESSAGE, code="invalid")

    for i in range(9, 11):
        value = sum(cpf[num] * ((i + 1) - num) for num in range(i))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            raise ValidationError(INVALID_CPF_MESSAGE, code="invalid")

    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"

def validate_birthdate(value):
    """
    Valida a data de nascimento.
    
    Args:
        value (date): A data de nascimento a ser validada.
    
    Returns:
        date: A data de nascimento validada.
    
    Raises:
        ValidationError: Se a data de nascimento for maior que a data atual.
    """
    if value > date.today():
        raise ValidationError(
            INVALID_BIRTHDATE_MESSAGE,
            code="invalid_birth_date",
        )
    return value

def validate_name(value):
    """
    Valida o nome fornecido.
    
    Args:
        value (str): O nome a ser validado.
    
    Returns:
        str: O nome validado e formatado.
    
    Raises:
        ValidationError: Se o nome for inválido.
    """
    # Remove espaços extras e capitaliza cada palavra
    formatted_name = ' '.join(word.capitalize() for word in value.split())
    
    # Verifica se o nome tem pelo menos duas palavras
    if len(formatted_name.split()) < 2:
        raise ValidationError(
            "O nome deve conter pelo menos nome e sobrenome.",
            code="invalid_name",
        )
    
    # Verifica se o nome contém apenas letras e espaços
    if not all(char.isalpha() or char.isspace() for char in formatted_name):
        raise ValidationError(
            "O nome deve conter apenas letras e espaços.",
            code="invalid_name",
        )
    
    # Verifica o comprimento mínimo e máximo do nome
    if len(formatted_name) < 3 or len(formatted_name) > 100:
        raise ValidationError(
            "O nome deve ter entre 3 e 100 caracteres.",
            code="invalid_name",
        )
    
    return formatted_name       

def validate_email(value):
    """
    Valida o email fornecido.
    
    Args:
        value (str): O email a ser validado.
    
    Returns:
        str: O email validado.
    
    Raises:
        ValidationError: Se o email for inválido.
    """
    # Remove espaços em branco no início e no fim
    email = value.strip()
    
    # Verifica se o email contém '@' e '.'
    if '@' not in email or '.' not in email:
        raise ValidationError(
            "O email deve conter '@' e '.'.",
            code="invalid_email"
        )
    
    # Verifica o comprimento mínimo e máximo do email
    if len(email) < 5 or len(email) > 254:
        raise ValidationError(
            "O email deve ter entre 5 e 254 caracteres.",
            code="invalid_email"
        )
    
    # Verifica se o email segue um padrão básico
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise ValidationError(
            "O email fornecido não é válido.",
            code="invalid_email"
        )
    
    return email
