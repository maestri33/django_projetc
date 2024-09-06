from rest_framework import serializers
from .models import (
    Profile, Convention, Promoter, EducationalInstitution,
    GraduationData, PostGraduationData, MiddleSchoolData, ElementarySchoolData,
    ProfileAddress, ConventionAddress
)

class ProfileAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileAddress
        fields = '__all__'

class ConventionAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConventionAddress
        fields = '__all__'

class GraduationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = GraduationData
        fields = '__all__'

class PostGraduationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostGraduationData
        fields = '__all__'

class MiddleSchoolDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiddleSchoolData
        fields = '__all__'

class ElementarySchoolDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementarySchoolData
        fields = '__all__'

class EducationalInstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalInstitution
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    enderecos = ProfileAddressSerializer(many=True, read_only=True, source='addresses')
    dados_graduacao = GraduationDataSerializer(many=True, read_only=True, source='graduation_data')
    dados_pos_graduacao = PostGraduationDataSerializer(many=True, read_only=True, source='post_graduation_data')
    dados_ensino_medio = MiddleSchoolDataSerializer(many=True, read_only=True, source='middle_school_data')
    dados_ensino_fundamental = ElementarySchoolDataSerializer(many=True, read_only=True, source='elementary_school_data')

    class Meta:
        model = Profile
        fields = '__all__'

class ConventionSerializer(serializers.ModelSerializer):
    enderecos = ConventionAddressSerializer(many=True, read_only=True, source='addresses')

    class Meta:
        model = Convention
        fields = '__all__'

class PromoterSerializer(serializers.ModelSerializer):
    perfil = ProfileSerializer(read_only=True, source='profile')
    convenio = ConventionSerializer(read_only=True, source='convention')

    class Meta:
        model = Promoter
        fields = '__all__'

class EducationalProfileSerializer(serializers.Serializer):
    graduacao = GraduationDataSerializer(many=True)
    pos_graduacao = PostGraduationDataSerializer(many=True)
    ensino_medio = MiddleSchoolDataSerializer(many=True)
    ensino_fundamental = ElementarySchoolDataSerializer(many=True)

class ProfileDashboardSerializer(serializers.ModelSerializer):
    enderecos = ProfileAddressSerializer(many=True, read_only=True, source='addresses')
    dados_educacionais = EducationalProfileSerializer(read_only=True, source='*')
    convenios = ConventionSerializer(many=True, read_only=True)
    promotores = PromoterSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

class ConventionDashboardSerializer(serializers.ModelSerializer):
    enderecos = ConventionAddressSerializer(many=True, read_only=True, source='addresses')
    promotores = PromoterSerializer(many=True, read_only=True)

    class Meta:
        model = Convention
        fields = '__all__'

class SearchSerializer(serializers.Serializer):
    perfis = ProfileSerializer(many=True)
    convenios = ConventionSerializer(many=True)
    promotores = PromoterSerializer(many=True)

class ReportSerializer(serializers.Serializer):
    total_perfis = serializers.IntegerField()
    total_convenios = serializers.IntegerField()
    total_promotores = serializers.IntegerField()
    total_instituicoes_ensino = serializers.IntegerField()

class EducationStatsSerializer(serializers.Serializer):
    total_perfis = serializers.IntegerField()
    perfis_com_graduacao = serializers.IntegerField()
    perfis_com_pos_graduacao = serializers.IntegerField()
    porcentagem_graduacao = serializers.FloatField()
    porcentagem_pos_graduacao = serializers.FloatField()

class PromoterPerformanceSerializer(serializers.Serializer):
    nome = serializers.CharField()
    convenio = serializers.CharField()
    contagem_leads = serializers.IntegerField()
    # Adicione mais métricas de desempenho conforme necessário