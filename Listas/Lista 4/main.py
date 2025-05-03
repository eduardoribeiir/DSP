import yaml
import logging
import json

config = {}

with open('config.yaml', 'r') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

logging.basicConfig(format=config["logging"]["format"], level=config["logging"]["level"], filename=config["logging"]["file"])

logger = logging.getLogger(__name__)

data = []

fileName = config["data"]["file"]

with open(fileName) as file:
    logger.info(f"Arquivo JSON '{fileName}' carregado com sucesso.")
    data = json.load(file)

def checkProperties(item):
    for key in item:
        if item[key] == None:
            return False
    return True

for item in data:
    isValid = checkProperties(item)
    
    if isValid:
        logger.info(f"Processando registro: '{item}'")
    else:
        logger.warning(f"Erro no registro: Dado inválido: '{item}'")