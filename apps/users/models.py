import hashlib
import uuid
from functools import cached_property

from allauth.account.models import EmailAddress
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.helpers import validate_profile_picture

# Importações necessárias
import hashlib
import uuid
from functools import cached_property

from allauth.account.models import EmailAddress
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.helpers import validate_profile_picture

# Função para gerar um nome de arquivo único para o avatar
# Isso evita sobrescrever arquivos existentes e resolve problemas de cache
def _get_avatar_filename(instance, filename):
    """Usa um nome de arquivo aleatório para evitar sobrescrever arquivos existentes e resolver problemas de cache."""
    return f'profile-pictures/{uuid.uuid4()}.{filename.split(".")[-1]}'

# Modelo de usuário personalizado
class CustomUser(AbstractUser):
    """
    Adicione campos adicionais ao modelo de usuário aqui.
    """
    #TODO: Vincular o usuário ao perfil, booleano indicando acesso está liberado ou não, tipo de usuario (choices) e código externo (criar função com ia da grop para sugerir um código)


    # Campo para armazenar o avatar do usuário
    avatar = models.FileField(upload_to=_get_avatar_filename, blank=True, validators=[validate_profile_picture])

    def __str__(self):
        """Retorna uma representação em string do usuário"""
        return f"{self.get_full_name()} <{self.email or self.username}>"

    def get_display_name(self) -> str:
        """Retorna o nome de exibição do usuário"""
        if self.get_full_name().strip():
            return self.get_full_name()
        return self.email or self.username

    @property
    def avatar_url(self) -> str:
        """Retorna a URL do avatar do usuário ou um avatar padrão do Gravatar"""
        if self.avatar:
            return self.avatar.url
        else:
            return "https://www.gravatar.com/avatar/{}?s=128&d=identicon".format(self.gravatar_id)

    @property
    def gravatar_id(self) -> str:
        """Calcula o ID do Gravatar para o usuário"""
        # https://en.gravatar.com/site/implement/hash/
        return hashlib.md5(self.email.lower().strip().encode("utf-8")).hexdigest()

    @cached_property
    def has_verified_email(self):
        """Verifica se o usuário tem um e-mail verificado"""
        return EmailAddress.objects.filter(user=self, verified=True).exists()

# Nota: Alguns termos técnicos como 'avatar', 'email' e nomes de métodos foram mantidos em inglês para manter a consistência do código.























