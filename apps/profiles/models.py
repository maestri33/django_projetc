from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from .validators import validate_birthdate, validate_name, validate_cpf, validate_phone, validate_email
from .choices import (GENDER_CHOICES, CIVIL_STATUS_CHOICES, CIVIL_CERTIFICATE_TYPE_CHOICES, PROFILE_DOCUMENT_CHOICES, INSTRUCTION_LEVEL_CHOICES, STATE_CHOICES, EDUCATIONAL_INSTITUTION_TYPE_CHOICES, EDUCATIONAL_INSTITUTION_NATURE_CHOICES, GRADUATION_TYPE_CHOICES, POSTGRADUATION_TYPE_CHOICES, SITUATION_EDUCATION_CHOICES, ADDRESS_TYPE_CHOICES)

# Modelo de Perfil

class Profile(models.Model):
#ATENÇÃO:
#Esta é a principal entidade do sistema, praticamente todos outros modelos estão relacionados a ela.
#Todos dados colhidos, quer seja de clientes, usuarios ou leads, estão salvos nesta tabela.

    name = models.CharField(
        max_length=100,
        validators=[validate_name],
        help_text=("Insira seu nome completo."),
        verbose_name=("Nome"),
        null=False,
        blank=False,
    ) 
    birth_date = models.DateField(
        validators=[validate_birthdate],
        help_text=("Insira aqui o dia, mês e ano em que você nasceu."),
        verbose_name=("Data de Nascimento"),
        null=False,
        blank=False,
    )
    cpf = models.CharField(
        max_length=14,
        unique=True,
        validators=[validate_cpf],
        help_text=('Insira aqui os números do seu CPF.'),
        verbose_name=("CPF - Cadastro de Pessoa Física"),
        null=False,
        blank=False,
    )
    phone = models.CharField(
        max_length=11,
        validators=[validate_phone],
        help_text=("Insira aqui qual o número do seu telefone com o DDD. Atenção, é necessário whatsapp ativo para validar o número."),
        verbose_name=("Telefone"),
        null=False,
        blank=False,
        unique=True,
    )
    email = models.EmailField(
        max_length=100,
        help_text=("Insira aqui o email que você deseja receber as notificações."),
        validators=[validate_email],
        verbose_name=("Email"),
        null=False,
        blank=False,
        unique=True,
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        help_text=("Selecione qual seu sexo."),
        verbose_name=("Gênero (Sexo)"),
        null=False,
        blank=False,
    )
    civil_status = models.CharField(
        max_length=1,
        choices=CIVIL_STATUS_CHOICES,
        help_text=("Selecione qual seu estado civil."),
        verbose_name=("Estado Civil"),
        null=False,
        blank=False,
    )
    civil_certificate = models.FileField(
        upload_to='civil_certificates/',
        verbose_name="Certidão Civil",
        help_text="Faça upload da certidão de nascimento, casamento ou divórcio. Formatos aceitos: PDF, JPG, PNG.",
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],
        null=True,
        blank=True
    )
    instruction_level = models.CharField(
        max_length=1,
        choices=INSTRUCTION_LEVEL_CHOICES,
        help_text=("Selecione qual seu nível de escolaridade."),
        verbose_name=("Escolaridade"),
        null=False,
        blank=False,
    )

    mother_name = models.CharField(
        max_length=100,
        help_text=("Insira o nome completo da sua mãe."),
        verbose_name=("Nome da Mãe"),
        null=False,
        blank=False,
    )
    birth_state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        help_text=("Selecione o estado onde você nasceu."),
        verbose_name=("Estado de Nascimento"),
        null=False,
        blank=False,
    )
    #TODO: Integrar com a API do IBGE para buscar as cidades.
    birth_city = models.CharField(
        max_length=100,
        help_text=("Selecione a cidade onde você nasceu."),
        verbose_name=("Cidade de Nascimento"),
        null=False,
        blank=False,
    )
    document_type = models.CharField(
        max_length=1,
        choices=PROFILE_DOCUMENT_CHOICES,
        help_text=("Selecione o tipo de documento."),
        verbose_name=("Tipo de Documento"),
        null=False,
        blank=False,
    )
    document = models.FileField(
        upload_to='documents/',
        verbose_name="Documento",
        help_text="Faça upload do documento de identificação (formatos aceitos: pdf, jpg, png).",
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],
    )
    photo = models.FileField(
        upload_to='profile_photos/',
        verbose_name="Foto",
        help_text="Faça upload de uma foto do perfil (formatos aceitos: jpg, png).",
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],)#TODO: Mudar FileField para ImageField, não mudei agora por erro no "pillow"
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=("Criado em"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=("Atualizado em"))
    class Meta:
        verbose_name = ("Perfil")
        verbose_name_plural = ("Perfis")
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)


class Convention(models.Model):
# Convenio é como uma franquia, ela irá gerir os promotores, que por sua vez irão gerir os leads e alunos, aqui devemos referenciar o perfil responsábel pelo convenio e depois dados do cnpj.
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='conventions', verbose_name="Perfil", help_text="Selecione o perfil que o convênio pertence.")
    cnpj = models.CharField(max_length=18, verbose_name="CNPJ", help_text="Insira aqui o CNPJ do convênio.") #criar validador para cnpj e buscar dados usando a API.
    name = models.CharField(max_length=100, verbose_name="Nome Fantasia", help_text="Insira aqui o nome fantasia da pessoa jurídica.")
    state_registration = models.CharField(max_length=100, verbose_name="Inscrição Estadual", help_text="Insira aqui a inscrição estadual da pessoa jurídica.")
    city_registration = models.CharField(max_length=100, verbose_name="Inscrição Municipal", help_text="Insira aqui a inscrição municipal da pessoa jurídica.")
    #TODO: Criar função com groq para sugerir o external_reference, o mesmo é importante por será usado para identificar o convênio e promoções, o mesmo deve ser obrigatorio, unico, e com tamanho limitado.
    convention_reference = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name="Referência Externa", help_text="Crie um código para identificar o convênio, o mesmo deve ser único e não pode ser alterado posteriormente.")
    asaas_token = models.CharField(max_length=100, verbose_name="Token Asaas", help_text="Insira aqui o token da Asaas do convênio.", null=True, blank=True)
    contract_convention = models.FileField(upload_to='convention_contracts/',verbose_name="Contrato de Convênio",help_text="Faça upload do contrato de convênio. Apenas formato PDF é aceito.",validators=[FileExtensionValidator(allowed_extensions=['pdf'])],null=True,blank=True)

    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    class Meta:
        verbose_name = ("Convênio")
        verbose_name_plural = ("Convênios")
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

class Promoter(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='promoters', verbose_name="Perfil", help_text="Selecione o perfil que o promotor pertence.", null=True, blank=True)
    convention = models.ForeignKey(Convention, on_delete=models.CASCADE, related_name='promoters', verbose_name="Convênio", help_text="Selecione o convênio que o promotor pertence.", null=True, blank=True)
    promoter_reference = models.CharField(max_length=15, unique=True, null=False, blank=False, verbose_name="Referência Externa", help_text="Crie um código para identificar o promotor, o mesmo deve ser único e não pode ser alterado posteriormente.")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    mercadopago_token = models.CharField(max_length=100, verbose_name="Token Mercado Pago", help_text="Insira aqui o token do Mercado Pago do promotor.", null=True, blank=True)
    contract_promoter = models.FileField(upload_to='promoter_contracts/',verbose_name="Contrato do Promotor",help_text="Faça upload do contrato de acordo com o promotor. Apenas formato PDF é aceito.",validators=[FileExtensionValidator(allowed_extensions=['pdf'])],null=True,blank=True)
    
    
    class Meta:
        verbose_name = ("Promotor")
        verbose_name_plural = ("Promotores")
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)
    #Promotores serão os usuários que irão gerenciar os leads e alunos, eles devem ter um perfil comum.




class AbstractAddress(models.Model):
    street = models.CharField(max_length=100, verbose_name="Rua", help_text="Insira aqui o nome da rua, avenida, etc.")
    number = models.CharField(max_length=10, verbose_name="Número", help_text="Insira aqui o número do local.")
    complement = models.CharField(max_length=100, verbose_name="Complemento", help_text="Insira aqui o complemento do local, se houver.", blank=True)  # Adicionado blank=True
    neighborhood = models.CharField(max_length=100, verbose_name="Bairro", help_text="Insira aqui o bairro do local.")
    city = models.CharField(max_length=100, verbose_name="Cidade", help_text="Insira aqui a cidade do local.")
    state = models.CharField(max_length=2, choices=STATE_CHOICES, verbose_name="Estado", help_text="Selecione o estado do local.")
    zip_code = models.CharField(max_length=9, verbose_name="CEP", help_text="Insira aqui o CEP do local.")
    type = models.CharField(max_length=1, choices=ADDRESS_TYPE_CHOICES, verbose_name="Tipo de Endereço", help_text="Selecione o tipo de endereço do local.")
    address_comprovation = models.FileField(upload_to='convention_address_comprovations/',verbose_name="Comprovante de Endereço",help_text="Faça upload do comprovante de endereço do convênio (ex: conta de luz, água, etc.). Formatos aceitos: PDF, JPG, PNG.",validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],null=True,blank=True)   
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    #TODO: Integrar com a API do IBGE para buscar as cidades.
    
    class Meta:
        abstract = True

class ProfileAddress(AbstractAddress):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='addresses', verbose_name="Perfil", help_text="Selecione o perfil que o endereço pertence.")
    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

class ConventionAddress(AbstractAddress):
    convention = models.ForeignKey('Convention', on_delete=models.CASCADE, related_name='addresses', verbose_name="Convênio", help_text="Selecione o convênio que o endereço pertence.")
    
    class Meta:
        verbose_name = "Endereço do Convênio"
        verbose_name_plural = "Endereços dos Convênios"

class EducationalInstitution(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome da Instituição", help_text="Insira aqui o nome da instituição.")
    cnpj = models.CharField(max_length=18, verbose_name="CNPJ", help_text="Insira aqui o CNPJ da instituição.")
    type = models.CharField(max_length=1, choices=EDUCATIONAL_INSTITUTION_TYPE_CHOICES, verbose_name="Tipo de Instituição", help_text="Selecione o tipo de instituição.")
    nature = models.CharField(max_length=1, choices=EDUCATIONAL_INSTITUTION_NATURE_CHOICES, verbose_name="Natureza da Instituição", help_text="Selecione a natureza da instituição.")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    class Meta:
        verbose_name = "Instituição de Ensino"
        verbose_name_plural = "Instituições de Ensino"

class EducationalInstitutionAddress(AbstractAddress):
    educational_institution = models.ForeignKey(EducationalInstitution, on_delete=models.CASCADE, related_name='addresses', verbose_name="Instituição de Ensino", help_text="Selecione a instituição de ensino que o endereço pertence.")
    
    class Meta:
        verbose_name = "Endereço da Instituição de Ensino"
        verbose_name_plural = "Endereços das Instituições de Ensino"

from django.db import models

# ... (outras importações e modelos permanecem inalterados)

class AbstractEducationalProfile(models.Model):
    educational_institution = models.ForeignKey(
        EducationalInstitution, 
        on_delete=models.CASCADE,
        related_name='%(class)s_profiles',
        verbose_name="Instituição de Ensino",
        help_text="Selecione a instituição de ensino que a escolaridade pertence."
    )
    type = models.CharField(max_length=1, choices=GRADUATION_TYPE_CHOICES, verbose_name="Tipo de Graduação", help_text="Selecione o tipo de graduação.")
    status = models.CharField(max_length=1, choices=SITUATION_EDUCATION_CHOICES, verbose_name="Situação da Escolaridade", help_text="Selecione a situação da escolaridade.")
    start_date = models.DateField(verbose_name="Data de Início", help_text="Insira aqui a data de início da escolaridade.")
    end_date = models.DateField(verbose_name="Data de Conclusão", help_text="Insira aqui a data de conclusão da escolaridade.", null=True, blank=True)
    document_historic = models.FileField(upload_to='education_historics/', verbose_name="Histórico Escolar", help_text="Insira aqui o documento do histórico escolar.")
    document_certificate = models.FileField(upload_to='education_certificates/', verbose_name="Certificado", help_text="Insira aqui o documento do certificado/diploma.")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")
    
    class Meta:
        abstract = True
        verbose_name = "Escolaridade"
        verbose_name_plural = "Escolaridades"

class GraduationData(AbstractEducationalProfile):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='graduation_data', verbose_name="Perfil", help_text="Selecione o perfil que a graduação pertence.")
    course = models.CharField(max_length=100, verbose_name="Curso", help_text="Insira o nome do curso.")
    
    class Meta:
        verbose_name = "Graduação"
        verbose_name_plural = "Graduações"

class PostGraduationData(AbstractEducationalProfile):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='post_graduation_data', verbose_name="Perfil", help_text="Selecione o perfil que a pós-graduação pertence.")
    course = models.CharField(max_length=100, verbose_name="Curso", help_text="Insira o nome do curso.")
    graduation_type = models.CharField(max_length=1, choices=POSTGRADUATION_TYPE_CHOICES, verbose_name="Tipo de Pós-Graduação", help_text="Selecione o tipo de pós-graduação.")
    
    class Meta:
        verbose_name = "Pós-Graduação"
        verbose_name_plural = "Pós-Graduações"

class MiddleSchoolData(AbstractEducationalProfile):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='middle_school_data', verbose_name="Perfil", help_text="Selecione o perfil que a escola pertence.")
    
    class Meta:
        verbose_name = "Ensino Médio"
        verbose_name_plural = "Ensino Médio"

class ElementarySchoolData(AbstractEducationalProfile):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='elementary_school_data', verbose_name="Perfil", help_text="Selecione o perfil que a escola pertence.")
    
    class Meta:
        verbose_name = "Ensino Fundamental"
        verbose_name_plural = "Ensino Fundamental"

    #TODO: Fase2 - Criar função que 1 - recebe a foto da certidão, 2 - identifica o tipo, 3 - identifica o/os nome/s, 5 - compara com o nome informado, se diferente retorna informando o erro
    #  6 - identifica a data de nascimento do individuo com nome validado, 7 Encontra data de nascimento, nome da mãe, cidade e estado onde nasceu, 8 - Compara o nome da certidão com respectivas certtidões para cada situação civil, nascimento = solteiro, casamento = casado, divorcio = divorciado, casamento com óbto do conjuge averbada = viuvo
    #  9 - insere dados encontrados em profile, atualiza e retorna para o usuario o sucesso.

    #Seguir mesma lógica para outros documentos.



