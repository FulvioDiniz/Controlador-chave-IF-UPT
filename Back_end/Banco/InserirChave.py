import sys
import os
from .ConexãoPost import ConectarBanco

table_name = "chave"

create_table_query_chave = '''
CREATE TABLE chave_table (
    nome VARCHAR(255) NOT NULL,
    situacao boolean NOT NULL
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

insere_chave("chave1", True)
