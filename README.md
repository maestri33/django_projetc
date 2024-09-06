

# maestri-mvp

Juntos dia após dia crescemos dentro de um propósito. Acreditamos que a educação é o maior instrumento que Deus usa para mudar o mundo.

## Instalação - Docker

A maneira mais fácil de começar é com o [Docker](https://www.docker.com/).

Basta [instalar o Docker](https://www.docker.com/get-started) e
[Docker Compose](https://docs.docker.com/compose/install/)
e então executar:

```
make init
```

Isso iniciará um banco de dados, servidor web, worker do Celery e broker Redis, e executará suas migrações.

Você pode então acessar [localhost:8000](http://localhost:8000/) para visualizar o aplicativo.

*Nota: se você receber um erro, certifique-se de ter um arquivo `.env`, ou crie um baseado no `.env.example`.*

### Usando o Makefile

Você pode executar `make` para ver outras funções auxiliares, e pode visualizar o código-fonte
do arquivo caso precise executar comandos específicos.

Por exemplo, você pode executar comandos de gerenciamento em contêineres usando o mesmo método 
usado no `Makefile`. Por exemplo:

```
docker compose exec web python manage.py createsuperuser
```

## Instalação - Nativa

Você também pode instalar/executar o aplicativo diretamente em seu sistema operacional usando as instruções abaixo.

Configure um ambiente virtual e instale os requisitos
(este exemplo usa [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)):

```bash
mkvirtualenv src -p python3.11
pip install -r dev-requirements.txt
```

## Configurar banco de dados

*Se você estiver usando Docker, pode pular estas etapas.*

Crie um banco de dados chamado `src`.

```
createdb src
```

Crie as migrações do banco de dados:

```
./manage.py makemigrations
```

Crie as tabelas do banco de dados:

```
./manage.py migrate
```

## Executando o servidor

**Docker:**

```bash
make start
```

**Nativo:**

```bash
./manage.py runserver
```

## Construindo o front-end

Para construir os arquivos JavaScript e CSS, primeiro instale os pacotes npm:

**Docker:**

```bash
make npm-install
```

**Nativo:**

```bash
npm install
```

Em seguida, construa (e observe as alterações localmente):

**Docker:**

```bash
make npm-watch
```

**Nativo:**

```bash
npm run dev-watch
```

## Executando o Celery

O Celery pode ser usado para executar tarefas em segundo plano.
Se você usar o Docker, ele iniciará automaticamente.

Você pode executá-lo usando:

```bash
celery -A src worker -l INFO --pool=solo
```

Ou com celery beat (para tarefas agendadas):

```bash
celery -A src worker -l INFO -B --pool=solo
```

Nota: Usar o pool `solo` é recomendado para desenvolvimento, mas não para produção.

## Configuração de Autenticação Google

Para configurar a Autenticação Google, siga as [instruções aqui](https://docs.allauth.org/en/latest/socialaccount/providers/google.html).

## Instalando hooks de commit do Git

Para instalar os hooks de commit do Git, execute o seguinte:

```shell
$ pre-commit install --install-hooks
```

Uma vez instalados, eles serão executados em cada commit.

Para mais informações, consulte a [documentação](https://docs.saaspegasus.com/code-structure.html#code-formatting).

## Executando Testes

Para executar testes:

**Docker:**

```bash
make test
```

**Nativo:**

```bash
./manage.py test
```

Ou para testar um aplicativo/módulo específico:

**Docker:**

```bash
docker compose exec web python manage.py test apps.utils.tests.test_slugs
```

**Nativo:**

```bash
./manage.py test apps.utils.tests.test_slugs
```

Em sistemas baseados em Linux, você pode observar as alterações usando o seguinte:

**Docker:**

```bash
find . -name '*.py' | entr docker compose exec web python manage.py test apps.utils.tests.test_slugs
```

**Nativo:**

```bash
find . -name '*.py' | entr python ./manage.py test apps.utils.tests.test_slugs
```