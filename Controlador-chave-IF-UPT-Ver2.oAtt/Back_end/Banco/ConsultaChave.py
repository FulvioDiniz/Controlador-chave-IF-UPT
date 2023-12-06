# author : Fulvio Diniz Santos
from typing import List, Tuple
from .ConexãoPost import ConectarBanco

def consulta_chave() -> List[Tuple[str, str]]:
    conn = ConectarBanco()
    cur = conn.cursor()
    cur.execute("SELECT nome, situacao FROM chave_table where situacao = 'true'")
    
    lista_chaves = cur.fetchall()

    # Feche a conexão com o banco de dados
    conn.close()

    return lista_chaves

def pesquisa_chave(nome_chave):
    conn = ConectarBanco()
    cur = conn.cursor()
    cur.execute("SELECT nome, status FROM chave_table WHERE nome = %s", (nome_chave,))
    result = cur.fetchone()
    conn.close()

    if result:
        return {"nome": result[0], "status": result[1]}
    else:
        return {"message": "Chave não encontrada"}


