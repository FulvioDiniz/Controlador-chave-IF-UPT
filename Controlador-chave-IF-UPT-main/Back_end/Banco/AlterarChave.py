from .ConexãoPost import ConectarBanco


def altera_nome_chave(antigo_nome, novo_nome):
    conn = ConectarBanco()
    cur = conn.cursor()
    
    try:
        cur.execute("UPDATE chave_table SET nome = %s WHERE nome = %s", (novo_nome, antigo_nome))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao alterar o nome da chave: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()