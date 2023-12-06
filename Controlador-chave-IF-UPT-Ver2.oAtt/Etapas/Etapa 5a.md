# Etapa 5

1. Crie na pasta do banco de dados o seguinte codigo:

```python
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
```

1. Agora crie uma pagina HTML e use o css como desejar, segue os dois codigos:
    
    2.1 HTML e Vue.js(onde ocorre a ligação do back com front)
    

```python
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../Css/PgListaChave.css">
    <title>Controle de Chaves</title>
</head>

<body>
    <div id="app" class="container">
        <h1>Controle de Chaves</h1>
        <button @click="ButtonRegistrarChave" class="register-button">Registrar Nova Chave</button>
        <div class="search-bar">
            <input type="text" placeholder="Buscar por chave...">
        </div>
        <table>
            <tr>
                <th>Chave</th>
                <th>Status</th>
                <th>Empresta</th>
                <th>Recebe</th>
            </tr>
            <tr v-for="(key, index) in keys" :key="index">
                <td>{{ key.name }}</td>
                <td>{{ key.status }}</td>
                <td><button @click="ButtonEmprestar(key.name)" class="btn-emprestar">Emprestar</button></td>
                <td><button @click="ButtonReceber(key.name)" class="btn-receber">Receber</button></td>
            </tr>
        </table>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        new Vue({
            el: '#app',
            data: {
                keys: []
            },
            mounted() {
                const cachedData = localStorage.getItem('cachedKeys');
                if (cachedData) {
                    this.keys = JSON.parse(cachedData);
                } else {
                    // Se os dados não estiverem em cache, faça uma chamada para listar as chaves
                    this.Listar_chave();
                }
            },
            methods: {
                async Listar_chave() {
                    try {
                        const response = await axios.get('http://127.0.0.1:8000/chaves');
                        this.keys = response.data.map(item => {
                            return {
                                name: item[0],
                                status: item[1]
                            };
                        });
                        localStorage.setItem('cachedKeys', JSON.stringify(this.keys));

                    } catch (error) {
                        console.log(error);
                    }
                },
                async ButtonEmprestar(nome_chave) {
                    console.log('Chave emprestada:', nome_chave);
                    // Você pode adicionar a lógica para emprestar a chave aqui
                },

                async ButtonRegistrarChave() {
                    window.location.href = `http://127.0.0.1:8000/cadastro_chave`;
                }
            }
        });
    </script>
</body>

</html>
```

2.2 CSS

```python
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 0;
  }
  .container {
    max-width: 800px;
    margin: 20px auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
    position: relative;
  }
  h1 {
    color: #333;
    margin-bottom: 20px;
  }
  .register-button {
    background-color: #2196F3;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    position: absolute;
    top: 20px;
    right: 20px;
    transition: background-color 0.3s, color 0.3s;
  }
  .register-button:hover {
    background-color: #333;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  th, td {
    padding: 12px;
    text-align: center;
    border-bottom: 1px solid #ddd;
  }
  th {
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
  }
  td button {
    padding: 6px 12px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s, color 0.3s;
  }
  td button:hover {
    background-color: #333;
    color: white;
  }
  .btn-emprestar {
    background-color: #4CAF50;
    color: white;
  }
  .btn-receber {
    background-color: #FF5722;
    color: white;
  }
  .search-bar {
    margin-bottom: 15px;
  }
  .search-bar input[type="text"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    color: #333;
    transition: border-color 0.3s;
  }
  .search-bar input[type="text"]:focus {
    border-color: #4CAF50;
  }
```

3. Adicione um arquivo python em sua pasta backend

```python
import fastapi
from fastapi import Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from Banco.ConsultaChave import consulta_chave

# Obtém o caminho absoluto para a pasta 'Back_end'
back_end_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Adiciona o caminho à lista de caminhos do Python
sys.path.append(back_end_path)

app = fastapi.FastAPI()

# Caminho relativo ao diretório do frontend
templates_dir = os.path.join(back_end_path, "../Front_end/Html")

templates = Jinja2Templates(directory=templates_dir)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
    allow_credentials=True
)

@app.get("/chaves", response_class=HTMLResponse)
async def listar_chaves(request: Request):
    lista_chaves = consulta_chave()
    return JSONResponse(content=lista_chaves)

```
