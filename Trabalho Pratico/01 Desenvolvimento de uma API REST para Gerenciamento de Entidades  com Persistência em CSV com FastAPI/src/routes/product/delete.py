import csv
from src.local_logger import local_logger

async def delete_product(id: int):
    try:
        with open('database/produtos.csv', 'r') as arquivo_csv:
            reader_arquivo = csv.reader(arquivo_csv)
            next(reader_arquivo)
            rows = list(reader_arquivo)
            arquivo_csv.close()

        product_exists = False
        for row in rows:
            if int(row[0]) == id:
                product_exists = True
                break

        if not product_exists:
            local_logger.info(f"Produto {id} não encontrado.")

            return {"message": "Produto não encontrado"}

        with open('database/produtos.csv', 'w', newline='') as arquivo_csv:
            writer_arquivo = csv.writer(arquivo_csv)
            writer_arquivo.writerow(['id', 'nome', 'preco', 'quantidade', 'data_vencimento'])
            for row in rows:
                if int(row[0]) != id:
                    writer_arquivo.writerow(row)
            arquivo_csv.close()

        local_logger.info(f"Produto {id} removido com sucesso.")

        return {"message": "Produto removido com sucesso"}
    except Exception as e:
        local_logger.error(f"Erro ao remover produto: {e}")
        return {"message": "Erro ao remover produto"}