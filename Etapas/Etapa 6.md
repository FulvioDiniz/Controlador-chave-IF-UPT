# Etapa 5

1. Dentro da pasta Back_end e da pasta Banco crie uma pasta chamada **InserirChave.py: Dentro dela insira o codigo abaixo:**

```python
# Autor: Fulvio Diniz Santos
from .ConexãoPost import ConectarBanco

table_name = "chave_table"

create_table_query_chave = '''
CREATE TABLE chave_table (
    nome VARCHAR(255) NOT NULL,
    situacao boolean NOT NULL
);
'''

def valida_chave(nome_chave):
		if nome_chave != NULL
	    conn = ConectarBanco()
	    cur = conn.cursor()
	    cur.execute("SELECT * FROM chave_table WHERE nome = %s", (nome_chave,))
	    if cur.rowcount > 0:
	        return False
	    else:
	        return True
		else:
				return False

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

1. Agora partindo para Front. Dentro da pasta **Front_end e da pasta HTML crie uma nova pagina chamada  PgRegistarChave.html, e insira o codigo abaixo.**

```python
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f0f8ea; /* Cor de fundo verde claro */
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        
        #app {
            background-color: #fff; /* Cor de fundo branca */
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        
        h1 {
            color: #388e3c; /* Cor verde */
            margin-bottom: 20px;
            text-align: center;
        }
        
        form {
            display: flex;
            flex-direction: column;
        }
        
        label {
            font-weight: bold;
            margin-bottom: 4px;
        }
        
        input {
            padding: 8px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        
        button {
            background-color: #388e3c; /* Cor verde */
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        
        button:hover {
            background-color: #2e7d32; /* Cor verde mais escura no hover */
        }
        
        .error {
            color: #d32f2f; /* Cor vermelha */
            font-size: 14px;
            text-align: center;
            margin-top: 10px;
        }
        
    </style>
</head>

<body>
    <div id="app">
        <h1>Registra Chave</h1>
        <form @submit.prevent="Registro_Chave">
            <label for="username">Numero da chave</label>
            <input type="text" id="username" v-model="username" required>
            <br>
            <button type="submit">Cadastrar</button>
        </form>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        new Vue({
            el: '#app',
            data: {
                username: '',
                errorMessage: ''
            },
            methods: {
                async Registro_Chave() {
                    try {
                        const response = await axios.post('http://127.0.0.1:8000/registro_chave', {
                            username: this.username,
                        });
                        if (response.data.success) {
                            alert('Registration successful');
                        } else {
                            this.errorMessage = response.data.message;
                        }
                    
                    } catch (error) {
                        console.error('Error:', error);
                        this.errorMessage = 'An error occurred during registration';
                    }
                }
            }
        });
    </script>

</body>

</html>
```

1. Dentro da Pasta Back_end e da pasta **Controller execute o codigo da [Main.py](http://Main.py) abaixo:**

```python
import fastapi
from fastapi import Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import sys
from Banco.InserirChave import insere_chave

@app.post("/registro_chave")
async def registro_chave(credentials: dict):
    numero = credentials.get("username")
    validador = insere_chave(numero, True)
    if(validador):
        return {"message": "Chave cadastrada com sucesso!"}
    else:
        return {"message": "Chave já cadastrada!"}
    
    
    

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
```
