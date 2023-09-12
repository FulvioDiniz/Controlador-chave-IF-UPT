# 2a Etapa:

**Parte 1: Frontend com Vue.js**

1. **Instalação do Node.js e npm:**
Verifique se você possui o Node.js instalado. Caso contrário, instale-o através do gerenciador de pacotes da sua distribuição. Isso também instalará o npm, o gerenciador de pacotes para bibliotecas JavaScript.
2. **Instalação do Vue CLI:**
Abra o terminal e instale o Vue CLI globalmente usando o npm:
    
    ```bash
    bashCopy code
    npm install -g @vue/cli
    
    ```
    
3. **Criação do Projeto Vue:**
No terminal, navegue para a pasta onde deseja criar o projeto e execute o seguinte comando para criar um novo projeto Vue:
    
    ```bash
    bashCopy code
    vue create nome-do-projeto-frontend
    
    ```
    
    Siga as instruções para selecionar as opções desejadas, como o uso do router, linting, etc.
    
4. **Navegação para a Pasta do Projeto:**
Navegue para a pasta do projeto Vue recém-criada:
    
    ```bash
    bashCopy code
    cd nome-do-projeto-frontend
    
    ```
    
5. **Instalação de Dependências:**
Instale as dependências do projeto:
    
    ```bash
    bashCopy code
    npm install
    
    ```
    
6. **Execução do Servidor de Desenvolvimento:**
Inicie o servidor de desenvolvimento para o frontend:
    
    ```bash
    bashCopy code
    npm run serve
    
    ```
    

**Parte 2: Backend com FastAPI**

1. **Criação do Ambiente Virtual:**
Caso ainda não tenha instalado o Virtualenvwrapper, siga as instruções do tutorial anterior para instalá-lo e configurá-lo.
2. **Criação da Pasta do Projeto Backend:**
Crie uma pasta para o projeto backend e navegue até ela:
    
    ```bash
    bashCopy code
    mkdir nome-do-projeto-backend
    cd nome-do-projeto-backend
    
    ```
    
3. **Ativação do Ambiente Virtual:**
Ative o ambiente virtual criado anteriormente:
    
    ```bash
    bashCopy code
    workon projetofinal
    
    ```
    
4. **Instalação do FastAPI e Dependências:**
Instale o FastAPI e outras dependências usando o pip:
    
    ```bash
    bashCopy code
    pip install fastapi uvicorn
    
    ```
    
5. **Criação do Arquivo Principal:**
Crie um arquivo chamado **`main.py`** para definir a aplicação FastAPI. Um exemplo básico seria:
    
    ```python
    pythonCopy code
    from fastapi import FastAPI
    
    app = FastAPI()
    
    @app.get("/")
    def read_root():
        return {"message": "Hello, FastAPI!"}
    
    ```
    
6. **Execução do Servidor FastAPI:**
Inicie o servidor FastAPI usando o Uvicorn:
    
    ```bash
    bashCopy code
    uvicorn main:app --host 0.0.0.0 --port 8000
    
    ```