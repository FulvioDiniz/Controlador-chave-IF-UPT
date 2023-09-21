import fastapi
from fastapi import Request
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import sys
import os
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse

#oi heito
# Obtém o caminho absoluto para a pasta 'Back_end'
back_end_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Adiciona o caminho à lista de caminhos do Python
sys.path.append(back_end_path)

# Agora você pode importar 'InserirUsuario' normalmente
from Banco.InserirUsuario import insere_usuario
from Banco.VerificarLogin import valida_login
from Banco.InserirChave import insere_chave
from Banco.ConsultaChave import consulta_chave

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
        
    

@app.post("/login")
async def login(credentials: dict):
    username = credentials.get("username")
    password = credentials.get("password")
    validador = valida_login(username, password)
    print(validador)
    if validador:
        return {"success": True, "message": "Login realizado com sucesso!"}
    else:
        return {"success": False, "message": "Usuário ou senha incorretos!"}

    
@app.get("/inicial/{username}", response_class=HTMLResponse)
async def inicial(request: Request, username: str):
    return templates.TemplateResponse("PgInicialUser.html", {"request": request, "username": username})

@app.get("/chaves", response_class=HTMLResponse)
async def listar_chaves(request: Request):
    lista_chaves = consulta_chave()
    return JSONResponse(content=lista_chaves)


@app.get("/cadastro_chave", response_class=HTMLResponse)
async def cadastro_chave(request: Request):
    return templates.TemplateResponse("PgRegistarChave.html", {"request": request})

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
