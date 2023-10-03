# Etapa 4:

Criar e configurar o banco de dados:

1. Baixar a biblioteca: psycopg2

```python
pip install psycopg2
```

1. Na pasta backend crie um arquivo com nome ConexãoPost e seguir os seguintes passos.

```python
import psycopg2
```

1. Variáveis do banco de dados:

```python
dbname = "ControleChave"
user = ""
password = ""
host = ""  # ou o endereço do servidor PostgreSQL
port = ""       # porta padrão do PostgreSQL
```

1. Variavel e execução (Base: Usuario) banco de dados:

```python
table_name = "usuario"

table_exists_query = f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')"

# Consulta SQL para criar a tabela
create_table_query_usuario = '''
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL
);
'''
```

1. Conexão banco de dados:

```python
# Tenta estabelecer a conexão
def ConectarBanco():
    try:
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Conexão estabelecida com sucesso!")

        with connection.cursor() as cursor:
            # Verifica se a tabela já existe
            cursor.execute(table_exists_query)
            table_exists = cursor.fetchone()[0]
            
            # Se a tabela já existe, exibe uma mensagem
            if table_exists:
                print("A tabela já existe.")
            else:
                # Se a tabela não existe, cria a tabela
                cursor.execute(create_table_query_usuario)
                connection.commit()
                print("Tabela criada com sucesso!")
            return connection

    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
```

1. Na pasta backend crie um arquivo com nome: BancoUsuario  baixe as bibliotecas e siga os passos:

```python
pip install sys
pip install os
```

1. Utilizando bibliotecas e importando a conexão do banco:

```python
import sys
import os
from .ConexãoPost import ConectarBanco
```

1. Função insere usuário: 

```python
def insere_usuario(nome, email, senha):
    conn = ConectarBanco()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuario WHERE email = %s", (email,))
    if cur.rowcount > 0:
        return False
    else:
        cur.execute("INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s)", (nome, email, senha))
        conn.commit()
        cur.close()
        conn.close()
        return True
```

1. Na pasta backend crie um arquivo com nome: BancoChave para inserir chave e execute o codigo: 

```python
# Autor: Fulvio Diniz Santos
from .ConexãoPost import ConectarBanco

table_name = "chave_table"

create_table_query_chave = '''
CREATE TABLE chave_table (
    nome VARCHAR(255) NOT NULL,
    situacao boolean NOT NULL,
		status boolean NOT NULL
);
'''

def valida_chave(nome_chave):
    conn = ConectarBanco()
    cur = conn.cursor()
    cur.execute("SELECT * FROM chave_table WHERE nome = %s", (nome_chave,))
    if cur.rowcount > 0:
        return False
    else:
        return True

def insere_chave(nome_chave, situacao_chave):
    conn = ConectarBanco()
    cur = conn.cursor()
    # Verifica se a tabela já existe
    cur.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')")
    table_exists = cur.fetchone()[0]

    if table_exists:
        print("A tabela já existe.")
        if valida_chave(nome_chave):
            cur.execute("INSERT INTO chave_table (nome, situacao) VALUES (%s, %s)", (nome_chave, situacao_chave))
            conn.commit()
            cur.close()
            conn.close()
            print("Chave inserida com sucesso.")
        else:
            print("Chave já existe na tabela.")
            cur.close()
            conn.close()
            return False
    else:
        print("A tabela não existe. Criando tabela...")
        cur.execute(create_table_query_chave)
        conn.commit()
        print("Tabela criada com sucesso!")

        if valida_chave(nome_chave):
            cur.execute("INSERT INTO chave_table (nome, situacao) VALUES (%s, %s)", (nome_chave, situacao_chave))
            conn.commit()
            cur.close()
            conn.close()
            print("Chave inserida com sucesso.")
        else:
            print("Chave já existe na tabela.")
            cur.close()
            conn.close()
            return False
```

1. Na pasta backend crie um arquivo com nome: BancoServidor e execute o código:

```python
from .ConexãoPost import ConectarBanco

table_name = "Servidor"

table_exists_query = f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}')"

# Consulta SQL para criar a tabela
create_table_query_servidor = '''
CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
		cpf  VARCHAR(255) NOT NULL,
		
    email VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL
);
'''

def cria_BD_servidor:
	cur.execute(create_table_query_servidor)
  conn.commit()
```

1. Na pasta backend crie um arquivo com nome: BancoEmprestimo e insira o código:

```python
from ConexãoPost import ConectarBanco

table = "Emprestimo"

query_table = """
CREATE TABLE IF NOT EXISTS {0} (
    id SERIAL PRIMARY KEY,
    status BOOLEAN,
    data_criacao VARCHAR(255),
    data_devolucao VARCHAR(255),
    chave_id INTEGER REFERENCES Chave(id),
    servidor_id INTEGER REFERENCES Servidor(id)
);
""".format(table)

def create_table():
    con = ConectarBanco()
    cur = con.cursor()
    cur.execute(query_table)
    con.commit()
    con.close()
'''
```

1. Execute no main para utilizar as funções:

```jsx
from ConexãoPost import ConectarBanco

def Teste():
    con = ConectarBanco()
    cur = con.cursor()
    cur.execute("SELECT * FROM usuario")
    print(cur.fetchall())
    con.close()
    
Teste()
```

1. Verifique mensagem de sucesso:

```jsx
Conexão estabelecida com sucesso!
A tabela já existe.
```
