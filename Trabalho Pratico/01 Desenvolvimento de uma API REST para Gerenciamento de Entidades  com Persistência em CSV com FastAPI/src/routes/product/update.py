import csv
from src.local_logger import local_logger
from src.models.Product import Product

async def update_product(id: int, name: str, price: float, quantity: int, due_date: str):
    try:
        rows = []
        with open('database/produtos.csv', 'r') as arquivo_csv:
            reader_arquivo = csv.reader(arquivo_csv)
            next(reader_arquivo)
            for row in reader_arquivo:
                rows.append(Product(
                    id=int(row[0]),
                    name=row[1],
                    price=float(row[2]),
                    quantity=int(row[3]),
                    due_date=row[4]
                ))
            arquivo_csv.close()

        array_index_to_update = -1
        for row in rows:
            if row.id == id:
                array_index_to_update = rows.index(row)
                break

        if array_index_to_update == -1:
            local_logger.info(f"Produto {id} não encontrado.")

            return {"message": "Produto não encontrado"}

        rows[array_index_to_update].name = name
        rows[array_index_to_update].price = price
        rows[array_index_to_update].quantity = quantity
        rows[array_index_to_update].due_date = due_date
        with open('database/produtos.csv', 'w', newline='') as arquivo_csv:
            writer_arquivo = csv.writer(arquivo_csv)
            writer_arquivo.writerow(['id', 'nome', 'preco', 'quantidade', 'data_vencimento'])
            for row in rows:
                writer_arquivo.writerow([
                    row.id,
                    row.name,
                    row.price,
                    row.quantity,
                    row.due_date
                ])
            arquivo_csv.close()

        local_logger.info(f"Produto {id} atualizado com sucesso.")

        return {"message": "Produto atualizado com sucesso"}
    except Exception as e:
        local_logger.error(f"Erro ao atualizar produto: {e}")
        return {"message": "Erro ao atualizar produto"}