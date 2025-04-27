Entrar na pasta do projeto "01 Desenvolvimento de uma API REST para Gerenciamento de Entidades  com Persistência em CSV com FastA
PI"
Executar:
- python3 -m venv ./venv
  // Se der erro apontando que não foi possível encontrar python3.10-venv
- sudo apt install python3.10-venv
- python3 -m venv ./venv
- source ./venv/bin/activate
- pip install fastapi
- pip install -U pip
- pip install "uvicorn[standard]"
- uvicord main:app --reload

Rodar o servidor
- source ./venv/bin/activate
- uvicorn main:app --reload
