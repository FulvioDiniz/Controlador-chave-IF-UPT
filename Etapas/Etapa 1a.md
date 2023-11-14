# **Documentação de Configuração do Projeto**
**0. Antes de tudo utilize o comando e lembrem-se a cada atualização do terminal fecha e abre novamente:
```bash
sudo apt-get update
```
## **1. Configuração do pyenv**


### **1.1 Instalação do pyenv**

Para instalar o pyenv, execute o seguinte comando:

```bash
curl https://pyenv.run | bash

```

### **1.2 Configuração do pyenv no ~/.bashrc**

Abra o arquivo **`~/.bashrc`** para configurar o pyenv:

```bash
xed ~/.bashrc

```

Adicione o seguinte código ao final do arquivo para configurar o pyenv:

```bash
# Configuração do pyenv
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
export PYENV_VIRTUALENV_DISABLE_PROMPT=1

# Configuração do prompt do pyenv
eval "$(pyenv virtualenv-init -)"
pyenvVirtualenvUpdatePrompt() {
    RED='\[\e[0;31m\]'
    GREEN='\[\e[0;32m\]'
    BLUE='\[\e[0;34m\]'
    RESET='\[\e[0m\]'
    [ -z "$PYENV_VIRTUALENV_ORIGINAL_PS1" ] && export PYENV_VIRTUALENV_ORIGINAL_PS1="$PS1"
    [ -z "$PYENV_VIRTUALENV_GLOBAL_NAME" ] && export PYENV_VIRTUALENV_GLOBAL_NAME="$(pyenv global)"
    VENV_NAME="$(pyenv version-name)"
    VENV_NAME="${VENV_NAME##*/}"
    GLOBAL_NAME="$PYENV_VIRTUALENV_GLOBAL_NAME"

    # Versões não globais:
    COLOR="$BLUE"
    # Versão global:
    [ "$VENV_NAME" == "$GLOBAL_NAME" ] && COLOR="$RED"
    # Ambientes virtuais:
    [ "${VIRTUAL_ENV##*/}" == "$VENV_NAME" ] && COLOR="$GREEN"

    if [ -z "$COLOR" ]; then
        PS1="$PYENV_VIRTUALENV_ORIGINAL_PS1"
    else
        PS1="($COLOR${VENV_NAME}$RESET)$PYENV_VIRTUALENV_ORIGINAL_PS1"
    fi
    export PS1
}
export PROMPT_COMMAND="$PROMPT_COMMAND pyenvVirtualenvUpdatePrompt;"

```
## **1.3. Utilize seguinte comando**
´´´
sudo apt update && sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev llvm```

## **2. Instalação de Versões do Python**

Agora que o pyenv está configurado, você pode instalar as versões desejadas do Python. Por exemplo:

```bash
pyenv install 3.11.5
pyenv install 3.7.17

```

## **3. Instalação do Volta**

Volta é um gerenciador de versões do Node.js e npm. Para instalá-lo, siga as etapas abaixo:

```bash
curl https://get.volta.sh | bash

```

## **4. Instalação do Node.js e npm**

Você pode usar o Volta para instalar versões específicas do Node.js e npm:

```bash
volta install node
volta install npm
volta install node@20.5.1
volta install npm@9.8.0

```

## **5. Instalação do Docker**

O Docker é uma plataforma de virtualização de contêineres. Siga as etapas a seguir para instalá-lo:

### **5.1 Instalação de Dependências**

```bash
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common gnupg lsb-release

```

### **5.2 Adição da Chave GPG do Docker**

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

```

### **5.3 Adição do Repositório do Docker**

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu jammy stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

```

### **5.4 Atualização e Instalação do Docker**

```bash
sudo apt update && sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin

```

## **6. Configuração do Completions do Docker**

Adicione o suporte a completions do Docker ao seu shell:

```bash
sudo curl -L "https://raw.githubusercontent.com/docker/cli/$(curl -sL https://api.github.com/repos/docker/docker/releases/latest | grep tag_name | cut -d'"' -f 4)/contrib/completion/bash/docker" -o /etc/bash_completion.d/docker

```

## **7. Instalação do Docker Compose**

Instale o Docker Compose para gerenciar contêineres multi-serviço:

```bash
sudo apt install docker-compose

```

## **8. Instalação do Docker Desktop (Opcional)**

Se você estiver usando uma distribuição Linux que suporte Docker Desktop, pode instalá-lo com os seguintes comandos:

```bash
sudo apt install docker-desktop

```

## **9. Iniciar o Serviço Docker**

Inicie o serviço Docker após a instalação:

```bash
sudo service docker start

```

## **10. Criar e Executar o Contêiner Ubuntu com PostgreSQL**

Crie e execute um contêiner Docker com a imagem do Ubuntu e PostgreSQL:

```bash
sudo docker run -d --name ubuntu-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 postgres:latest

```
Para conectar-se ao banco de dados, execute o seguinte comando no terminal:

```bash
psql -h localhost -p 5432 -U postgres
```
Crie seu banco de dados substituindo "mihadatabase" para nome desejado
```bash
CREATE DATABASE minhabasededados;
```

## **11. Para melhor vizualização baixe em sua maquina o pgadmin4 e utilize o banco com as conexões criadas por lá. (Opcional - Recomendado) **

```bash
https://www.pgadmin.org/download/pgadmin-4-windows/

```



[FulvioDiniz - Overview](https://github.com/FulvioDiniz)
