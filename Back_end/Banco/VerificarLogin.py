import sys
import os

# Obtém o caminho absoluto para a pasta 'Back_end'
back_end_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Adiciona o caminho à lista de caminhos do Python
sys.path.append(back_end_path)

from .ConexãoPost import ConectarBanco

def valida_login(username, password):
    # Conecta ao banco de dados
    conn = ConectarBanco()
    # Obtém o cursor para executar as operações
    cursor = conn.cursor()
    # Executa a query
    cursor.execute("SELECT * FROM usuario WHERE nome = %s AND senha = %s", (username, password))
    # Obtém o resultado da query
    result = cursor.fetchone()
    # Fecha a conexão com o banco de dados
    conn.close()
    # Retorna True se o usuário existir e a senha estiver correta, False caso contrário
    return result is not None

if valida_login('Fulvio','123'):
    print('Login válido')
else:
    print('Login inválido')