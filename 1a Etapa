# 1a Etapa:

**Passo 1: Configuração Inicial**

1. **Atualização do Sistema:**
Abra o terminal e execute os seguintes comandos para atualizar a lista de pacotes e atualizar o sistema:
    
    ```bash
    bashCopy code
    sudo apt update
    sudo apt upgrade
    
    ```
    

1. **Instalação das Dependências Básicas:**
Instale algumas dependências básicas que serão necessárias mais tarde:
    
    ```bash
    bashCopy code
    sudo apt install curl git
    
    ```
    

**Passo 2: Configuração do Docker**

1. **Instalação do Docker:**
Instale o Docker para criar e gerenciar containers:
    
    ```bash
    bashCopy code
    sudo apt install docker.io
    
    ```
    
2. **Habilitar e Iniciar o Serviço Docker:**
Inicie e habilite o serviço Docker para iniciar automaticamente durante o boot:
    
    ```bash
    bashCopy code
    sudo systemctl enable docker
    sudo systemctl start docker
    
    ```
    

**Passo 3: Configuração do PostgreSQL**

1. **Instalação do PostgreSQL:**
Instale o PostgreSQL, um sistema de gerenciamento de banco de dados:
    
    ```bash
    bashCopy code
    sudo apt install postgresql postgresql-contrib
    
    ```
    
2. **Criar Banco de Dados e Usuário:**
Acesse o PostgreSQL e crie um banco de dados e um usuário para o projeto:
    
    ```bash
    bashCopy code
    sudo -u postgres psql
    CREATE DATABASE nomedobanco;
    CREATE USER nomeusuario WITH PASSWORD 'senhadousuario';
    ALTER ROLE nomeusuario SET client_encoding TO 'utf8';
    ALTER ROLE nomeusuario SET default_transaction_isolation TO 'read committed';
    ALTER ROLE nomeusuario SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE nomedobanco TO nomeusuario;
    \q
    
    ```
    

**Passo 4: Configuração do Vue.js**

1. **Instalação do Node.js:**
Instale o Node.js, necessário para desenvolvimento com Vue.js:
    
    ```bash
    bashCopy code
    sudo apt install nodejs npm
    
    ```
    
2. **Instalação do Vue CLI:**
Instale a interface de linha de comando do Vue.js:
    
    ```bash
    bashCopy code
    sudo npm install -g @vue/cli
    
    ```
    

**Passo 5: Configuração do FastAPI**

1. **Instalação do Python e pip:**
Verifique se o Python já está instalado. 
    
    ```bash
    bashCopy code
    sudo apt install python3-pip
    
    ```
    
2. **Instalação do Virtualenvwrapper:**
Instale o Virtualenvwrapper para gerenciar ambientes virtuais de forma mais conveniente:
    
    ```bash
    bashCopy code
    sudo apt install virtualenvwrapper
    
    ```
    
3. **Configuração do Virtualenvwrapper:**
Adicione as seguintes linhas ao final do seu arquivo **`~/.bashrc`** para configurar o Virtualenvwrapper:
    
    ```bash
    bashCopy code
    export WORKON_HOME=$HOME/.virtualenvs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    source /usr/local/bin/virtualenvwrapper.sh
    
    ```
    
4. **Criar e Ativar Ambiente Virtual:**
Atualize o terminal para aplicar as configurações ou execute **`source ~/.bashrc`**. Em seguida, crie e ative um ambiente virtual:
    
    ```bash
    bashCopy code
    mkvirtualenv projetofinal
    
    ```
    

**Passo 6: Configuração do Projeto com Docker, Vue.js, FastAPI e PostgreSQL**

1. **Clonar o Projeto:**
Clone o projeto do repositório usando o Git:
    
    ```bash
    bashCopy code
    git clone url_do_repositorio
    cd nome_do_projeto
    
    ```
    
2. **Configuração do Backend (FastAPI):**
Crie um arquivo **`requirements.txt`** contendo as dependências do projeto. Instale as dependências usando o pip:
    
    ```bash
    bashCopy code
    pip install -r requirements.txt
    
    ```
    
3. **Configuração do Frontend (Vue.js):**
Navegue para a pasta do frontend e instale as dependências do projeto:
    
    ```bash
    bashCopy code
    cd frontend
    npm install
    
    ```
    
4. **Configuração do Docker:**
Crie um arquivo **`Dockerfile`** na raiz do projeto para definir a configuração do container Docker. Um exemplo básico de **`Dockerfile`** seria:
    
    ```sql
    sqlCopy code
    FROM python:3.9
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
    
    ```
    
5. **Criar e Executar Containers Docker:**
Crie e execute os containers Docker para o backend e o frontend, respectivamente:
    
    ```bash
    bashCopy code
    docker build -t projetofinal-backend .
    docker run -d -p 8000:8000 projetofinal-backend
    
    cd frontend
    npm run serve
    
    ```
    

[FulvioDiniz - Overview](https://github.com/FulvioDiniz)
