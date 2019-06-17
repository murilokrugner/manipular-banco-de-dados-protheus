# Conectando banco de dados SQL Server no Django 2x e Python 3x

![Logo Django](https://github.com/murilokrugner/manipular-banco-de-dados-protheus/blob/master/django-logo.jpg)

## Nesse repositório vós ensinareis a conectar o banco de dados SQL Server, do sistema ERP Protheus no seu projeto Django.

**Inicie seu ambiente virtual anaconda ou virtualenv para começar :)

### 1) - Instalando dependências

- **a)** - Primero precisamos instalar o ODBC com o comando abaixo:

`pip install django-pyodbc-azure`

Instalamos a unica dependêcia que precisamos para conectar o banco ao projeto :)

### 2) - Conectando banco o banco no settings.py

- **b)** - Vamos fazer a conexão do db no arquivo de configurações do seu projeto **settings.py**

```DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'Nome do seu banco de dados',
        'USER': 'Nome do usuário',
        'PASSWORD': 'Senha',
        'HOST': 'Nome da instancia do SQL Server a ser utilizada',
        'PORT': 'Número da porta de comunicação', #pode ser a default que o Django utiliza.
    },
}
```
Pronto! db conectado! agora precisamos migrar as tabelas existentes para os nossos **models.py**

### 3) - Migrando as tabelas existentes

- **a)** - Vamos usar o comando abaixo para migrar as tabelas, pois o Django vem com uma ferramenta chamada inspectdb que pode criar os            modelos introspectando o banco de dados existente. Você pode verificar a saida rodando este comando:

`python manage.py inspectdb`

Isso vai demorar alguns minutos...

Pronto! tabelas migradas! 

- **b)** - Agora iremos executar o seguinte comando para que possamos criar o arquivo **models.py** com as tabelas:

`python manage.py inspectdb > models.py`

Arquivo criado! substitua o arquivo existente do seu projeto, com o novo arquivo **models.py**

### 4) - Orientações

- **a)** - Indico fortemente que você **não** migre as tabelas nativas do Django no banco de dados SQL existente, pois é muito 
           provável que de algum conflito, e você não quer ter essa dor de cabeça de graça né? rs
           
- **b)** - Se você quer permitir que o Django gerencie o ciclo de vida das tabelas, é necessário alterar a opção managed para True                  (ou simplesmente removê-la porque True é o valor padrão).

- **c)** - Para resolver o problema de criarmos as tabelas do Django acidentalmente no banco existente, vamos conectar dois bancos
           de dados 
           
### 5) - Resultado

- **a)** Seu models.py irão ficar mais o menos assim:

![models](https://github.com/murilokrugner/manipular-banco-de-dados-protheus/blob/master/sc7010.jpg)

:)
