import sys
import os
from .ConexãoPost import ConectarBanco

# Obtém o caminho absoluto para a pasta 'Back_end'
back_end_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Adiciona o caminho à lista de caminhos do Python
sys.path.append(back_end_path)




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



