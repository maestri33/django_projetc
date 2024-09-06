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


# TODO: Implementar um signal para notificar o perfil do convênio quando um novo Promoter for criado
