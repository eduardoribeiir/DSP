import csv
from src.local_logger import local_logger

async def update_product(id: int, name: str, price: float, quantity: int, due_date: str):
    try:
        with open('database/produtos.csv', 'r') as arquivo_csv:
            reader_arquivo = csv.reader(arquivo_csv)
            next(reader_arquivo)
            rows = list(reader_arquivo)
            arquivo_csv.close()

        index_to_update = -1
        for index, row in enumerate(rows):
            if int(row[0]) == id:
                index_to_update = index
                break

        if index_to_update == -1:
            local_logger.info(f"Produto {id} não encontrado.")

            return {"message": "Produto não encontrado"}

        rows[index_to_update] = [id, name, price, quantity, due_date]

        with open('database/produtos.csv', 'w', newline='') as arquivo_csv:
            writer_arquivo = csv.writer(arquivo_csv)
            writer_arquivo.writerow(['id', 'nome', 'preco', 'quantidade', 'data_vencimento'])
            for row in rows:
                writer_arquivo.writerow(row)
            arquivo_csv.close()

        local_logger.info(f"Produto {id} atualizado com sucesso.")

        return {"message": "Produto atualizado com sucesso"}
    except Exception as e:
        local_logger.error(f"Erro ao atualizar produto: {e}")
        return {"message": "Erro ao atualizar produto"}