import fastapi
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Obtém o caminho absoluto para a pasta 'Back_end'
back_end_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Adiciona o caminho à lista de caminhos do Python
sys.path.append(back_end_path)

# Agora você pode importar 'InserirUsuario' normalmente
from Banco.InserirUsuario import insere_usuario

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
    allow_credentials=True
)



@app.post("/register")
async def register(credentials: dict):
    username = credentials.get("username")
    email = credentials.get("email")
    password = credentials.get("password")
    valido = insere_usuario(username, email, password)
    if valido:
        return {"message": "Usuário cadastrado com sucesso!"}
    else:   
        return {"message": "Usuário já cadastrado!"}
        
    

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
