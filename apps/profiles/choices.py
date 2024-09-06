GENDER_CHOICES = [
    ("M", "Masculino"),
    ("F", "Feminino"),
]

# Estado Civil
CIVIL_STATUS_CHOICES = [
    ("S", "Solteiro(a)"),
    ("C", "Casado(a)"),
    ("D", "Divorciado(a)"),
    ("V", "Viúvo(a)"),
]

CIVIL_CERTIFICATE_TYPE_CHOICES = [
    ("S", "Certidão de Nascimento"),
    ("C", "Certidao de Casamento"),
    ("D", "Certidão de Averbação de Divórcio"),
    ("V", "Certidão de Casamento"),
]

PROFILE_DOCUMENT_CHOICES = [ #RG ou CNH
    ("R", "RG"),
    ("C", "CNH"),
    ("P", "Passaporte"),
]

# Situação Educacional
SITUATION_EDUCATION_CHOICES = [
    ("C", "Cursando"),
    ("F", "Concluído"),
    ("X", "Cancelado"),
    ("T", "Trancado"),
]

# Tipo de Graduação
GRADUATION_TYPE_CHOICES = [
    ("B", "Bacharelado"),
    ("L", "Licenciatura"),
    ("T", "Tecnólogo"),
]

# Status Acadêmico
INSTRUCTION_LEVEL_CHOICES = [
    ("F", "Ensino Fundamental"),
    ("M", "Ensino Médio"),
    ("G", "Ensino Superior - Graduação"),
    ("P", "Ensino Superior - Pós-Graduação"),
]

# Tipo de Pós-Graduação
POSTGRADUATION_TYPE_CHOICES = [
    ("D", "Doutorado"),
    ("M", "Mestrado"),
    ("P", "Pós-Doutorado"),
]

STATE_CHOICES = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
]

#CHOICES PARA TIPOS DE ENDEREÇOS, PARA PF E PJ
ADDRESS_TYPE_CHOICES = [
    ("C", "Casa"),
    ("T", "Trabalho"),
    ("O", "Outro"),
    ("S", "Sede"),
    ("F", "Filial"),
    ]

#CHOICES PARA TIPOS DE INSTITUIÇÕES DE ENSINO
EDUCATIONAL_INSTITUTION_TYPE_CHOICES = [
    ("E", "Escola - Ensino Fundamental"),
    ("C", "Colégio - Ensino Médio"),
    ("S", "Instituição de Ensino Superior"),
]

#CHOICES PARA NATUREZA DA INSTITUIÇÃO DE ENSINO
EDUCATIONAL_INSTITUTION_NATURE_CHOICES = [
    ("P", "Pública"),
    ("R", "Privada"),
]