# **Criando o Projeto**

### **1. Configurar o Ambiente de Desenvolvimento**

Certifique-se de que o Node.js e o npm estejam instalados no seu sistema. Se não estiverem, siga as instruções no guia anterior para configurar o ambiente de desenvolvimento Node.js.

### **2. Inicializar o Projeto Vue.js**

```bash
bashCopy code
npm install -g @vue/cli
vue create frontend
mkdir frontend
cd frontend

```

Isso criará um novo projeto Vue.js chamado "nome-do-projeto-frontend" e o direcionará para o diretório do projeto.

### **3. Desenvolvimento Frontend**

Você pode começar a desenvolver seu aplicativo web Vue.js no diretório do projeto. Use um editor de código de sua escolha e implemente a lógica e os componentes necessários.

### **4. Executar o Servidor de Desenvolvimento**

Para iniciar o servidor de desenvolvimento utilize a extensão do vscode: Visual Studio Code Live Server





## **Criando o Projeto Backend com FastAPI**

### **1. Configurar o Ambiente de Desenvolvimento Python**

Certifique-se de que o Python e o pip estejam instalados no seu sistema. Além disso, siga as etapas do guia anterior para configurar o ambiente Python com pyenv.

### **2. Inicializar o Projeto FastAPI**

```bash
bashCopy code
pip install fastapi
pip install uvicorn
mkdir backend
cd backend

```

Crie um arquivo chamado **`main.py`** no diretório "nome-do-projeto-backend" para iniciar o projeto FastAPI.

### **3. Desenvolvimento Backend com FastAPI**

Desenvolva sua aplicação FastAPI no arquivo **`main.py`**. Configure rotas, modelos, lógica de negócios e outros aspectos do backend.

### **4. Executar o Servidor FastAPI**

Inicie o servidor FastAPI executando o seguinte comando no diretório do projeto FastAPI:

```bash
bashCopy code
uvicorn main:app --reload

```

Acesse **[http://localhost:8000](http://localhost:8000/)** em seu navegador para acessar a API do backend em desenvolvimento.
