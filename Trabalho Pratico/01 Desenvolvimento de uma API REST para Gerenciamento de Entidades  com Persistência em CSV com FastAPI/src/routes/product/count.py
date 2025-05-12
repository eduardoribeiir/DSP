import csv
from src.local_logger import local_logger

async def count_products():
    try:
        with open('database/produtos.csv', 'r') as arquivo_csv:
            reader_arquivo = csv.reader(arquivo_csv)
            next(reader_arquivo)
            rows = list(reader_arquivo)
            arquivo_csv.close()

        local_logger.info(f"Sucesso ao contar o total de produtos: {len(rows)}")

        return {"message": "Sucesso ao contar o total de produtos", "quantidade": len(rows)}
    except Exception as e:
        local_logger.error(f"Erro ao contar o total de produtos: {e}")
        return {"message": "Erro ao contar o total de produtos"}