
from .ConexãoPost import ConectarBanco

def exclui_chave(nome_chave):
    conn = ConectarBanco()
    cur = conn.cursor()
    
    try:
        cur.execute("UPDATE chave_table SET situacao = false WHERE nome = %s", (nome_chave,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao excluir a chave: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()