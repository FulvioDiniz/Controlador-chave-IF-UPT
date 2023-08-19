# author : Fulvio Diniz Santos
from .ConexãoPost import ConectarBanco

lista_chaves = []

def consulta_chave():
    conn = ConectarBanco()
    cur = conn.cursor()
    cur.execute("SELECT * FROM chave_table")
    if cur.rowcount > 0:
        for linha in cur.fetchall():
            lista_chaves.append(linha)
        return lista_chaves
    else:
        return "não possui chave no sistema"
    conn.close()

def pesquisa_chave(nome_chave):
    conn = ConectarBanco()
    cur = conn.cursor()
    cur.execute("SELECT * FROM chave_table WHERE nome = %s", (nome_chave,))
    if cur.rowcount > 0:
        return True
    else:
        return "não possui essa chave no sistema"
    

