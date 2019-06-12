# Conectando banco de dados SQL Server no Django 2x e Python 3x

## Nesse repositório vós ensinareis a conectar o banco de dados SQL Server, do sistema ERP Protheus no seu projeto Django.

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

- **a)** - Vamos usar o comando abaixo para migrar as tabelas, pois o Django vem com uma ferramenta chamada inspectdb que pode criar os              modelos introspectando o banco de dados existente. Você pode verificar a saida rodando este comando:

`python manage.py inspectdb`

Isso vai demorar alguns minutos...

Pronto! tabelas migradas! 

- **b)** - Agora iremos executar o seguinte comando para que possamos criar o arquivo **models.py** com as tabelas:

`python manage.py inspectdb > models.py`

Arquivo criado! substitua o arquivo existente do seu projeto, com o novo arquivo **models.py**
