import psycopg2

# Parâmetros de conexão
dbname = "ControleChave"
user = "postgres"
password = "230199"
host = "localhost"  # ou o endereço do servidor PostgreSQL
port = "5432"       # porta padrão do PostgreSQL

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



