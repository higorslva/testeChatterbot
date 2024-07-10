
# Tutorial de Configuração de Ambiente para Desenvolvimento de Chatbot [(#1)](https://github.com/higorslva/testeChatterbot/issues/1)

Este tutorial cobre a instalação de dependências essenciais e a configuração de um ambiente Python isolado para desenvolvimento de um chatbot. **Testado no Ubuntu 24.04**



## Passo 1: Instalar Dependências

Primeiro, instale as dependências necessárias no seu sistema. Abra um terminal e execute o seguinte comando:

```sh
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
```
No Arch Linux e derivados:
```sh
sudo pacman -S base-devel openssl zlib bzip2 readline sqlite wget curl llvm ncurses xz tk libffi python-pyopenssl git
```

## Passo 2: Instalar e Configurar o Pyenv

O Pyenv é uma ferramenta para gerenciar diferentes versões do Python. Execute o comando abaixo para instalar o Pyenv:

```sh
curl https://pyenv.run | bash
```

## Passo 3: Configurar o Ambiente do Pyenv

Adicione as seguintes linhas no final do seu arquivo `~/.bashrc` para configurar o Pyenv corretamente. Abra o arquivo com o editor de texto `nano`:

```sh
nano ~/.bashrc
```

Adicione as seguintes linhas ao final do arquivo `~/.bashrc`:

```sh
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Salve e feche o arquivo (`Ctrl + O`, `Enter`, `Ctrl + X`).

Para aplicar as mudanças, recarregue o `bashrc`:

```sh
source ~/.bashrc
```

## Passo 4: Instalar e Configurar o Python 3.7.9 com Pyenv

Use o Pyenv para instalar o Python 3.7.9 para ser utilizado no seu projeto:

```sh
pyenv install 3.7.9
```

## Passo 5: Criar e Configurar o Ambiente Virtual

Crie um novo diretório para o seu projeto de chatbot e navegue até ele:

```sh
mkdir chatbot
cd chatbot
```
Instale localmente o Python 3.7.9 na pasta
```sh
pyenv local 3.7.9
```
Crie um ambiente virtual Python chamado `chatterbot`:

```sh
python -m venv chatterbot
```

Ative o ambiente virtual:

```sh
source chatterbot/bin/activate
```

## Passo 6: Instalar Pacotes Necessários

Dentro do ambiente virtual, instale os pacotes necessários para o desenvolvimento do chatbot. Note que a versão do Spacy deve ser a 2.3.7:

```sh
pip install spacy==2.3.7
python -m spacy download en
pip install chatterbot
pip install chatterbot_corpus
```

## Passo 7: Executar o Chatbot

Agora você pode criar seu script Python (`chatbot.py`) e executá-lo no ambiente virtual. Por exemplo:

```sh
python chatbot.py
```

Certifique-se de que seu arquivo `chatbot.py` esteja no diretório `chatbot` e que o ambiente virtual esteja ativado antes de executar o script.
