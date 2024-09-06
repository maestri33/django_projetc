from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile, ProfileAddress, ElementarySchoolData, MiddleSchoolData, GraduationData, PostGraduationData, Convention, ConventionAddress

@receiver(post_save, sender=Profile)
def create_profile_address(sender, instance, created, **kwargs):
    """
    Este signal cria automaticamente um endereço para o perfil quando um novo perfil é criado.
    """
    if created:
        ProfileAddress.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def create_educational_profile(sender, instance, created, **kwargs):
    """
    Este signal cria automaticamente os dados educacionais correspondentes ao nível de instrução
    do perfil quando um novo perfil é criado.
    """
    if created:
        instruction_level = instance.instruction_level
        if instruction_level == 'F':
            ElementarySchoolData.objects.create(profile=instance)
        elif instruction_level == 'M':
            MiddleSchoolData.objects.create(profile=instance)
        elif instruction_level == 'G':
            GraduationData.objects.create(profile=instance)
        elif instruction_level == 'P':
            PostGraduationData.objects.create(profile=instance)

        
@receiver(post_save, sender=Convention)
def create_convention_address(sender, instance, created, **kwargs):
    """
    Este signal cria automaticamente um endereço para o convênio quando um novo convênio é criado.
    """
    if created:
        ConventionAddress.objects.create(convention=instance)

# Importações adicionais necessárias
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction

# Modificação dos signals existentes para incluir tratamento de erros e transações

@receiver(post_save, sender=Profile)
def create_profile_address(sender, instance, created, **kwargs):
    """
    Este signal cria automaticamente um endereço para o perfil quando um novo perfil é criado.
    """
    if created:
        try:
            with transaction.atomic():
                ProfileAddress.objects.create(profile=instance)
        except Exception as e:
            print(f"Erro ao criar endereço do perfil: {str(e)}")

@receiver(post_save, sender=Profile)
def create_educational_profile(sender, instance, created, **kwargs):
    """
    Este signal cria automaticamente os dados educacionais correspondentes ao nível de instrução
    do perfil quando um novo perfil é criado.
    """
    if created:
        try:
            with transaction.atomic():
                instruction_level = instance.instruction_level
                if instruction_level == 'F':
                    ElementarySchoolData.objects.create(profile=instance)
                elif instruction_level == 'M':
                    MiddleSchoolData.objects.create(profile=instance)
                elif instruction_level == 'G':
                    GraduationData.objects.create(profile=instance)
                elif instruction_level == 'P':
                    PostGraduationData.objects.create(profile=instance)
        except Exception as e:
            print(f"Erro ao criar dados educacionais do perfil: {str(e)}")

@receiver(post_save, sender=Convention)
def create_convention_address(sender, instance, created, **kwargs):
    """
    Este signal cria automaticamente um endereço para o convênio quando um novo convênio é criado.
    """
    if created:
        try:
            with transaction.atomic():
                ConventionAddress.objects.create(convention=instance)
        except Exception as e:
            print(f"Erro ao criar endereço do convênio: {str(e)}")

# Adição de um novo signal para notificar o perfil do convênio quando um novo Promoter for criado

from .models import Promoter
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Promoter)
def notify_convention_profile(sender, instance, created, **kwargs):
    """
    Este signal notifica o perfil do convênio quando um novo Promoter é criado.
    """
    if created:
        try:
            convention = instance.convention
            if convention and convention.profile:
                profile = convention.profile
                subject = "Novo Promotor Criado"
                message = f"Um novo promotor foi criado para o seu convênio: {instance.promoter_reference}"
                from_email = settings.DEFAULT_FROM_EMAIL
                recipient_list = [profile.user.email]
                
                send_mail(subject, message, from_email, recipient_list)
        except ObjectDoesNotExist:
            print("Erro: Convênio ou perfil associado não encontrado.")
        except Exception as e:
            print(f"Erro ao notificar perfil do convênio: {str(e)}")



# TODO: Implementar um signal para notificar o perfil do convênio quando um novo Promoter for criado
