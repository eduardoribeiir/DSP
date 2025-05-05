import csv
from src.local_logger import local_logger

async def create_product(name: str, price: float, quantity: int, due_date: str = None):
    try:
        new_id = 1

        with open('database/produtos.csv', 'r') as arquivo_csv:
            reader_arquivo = csv.reader(arquivo_csv)
            next(reader_arquivo)
            for row in reader_arquivo:
                if int(row[0]) >= new_id:
                    new_id = int(row[0]) + 1
            arquivo_csv.close()
        
        with open('database/produtos.csv', 'a', newline='') as arquivo_csv:
            writer_arquivo = csv.writer(arquivo_csv)
            writer_arquivo.writerow([new_id, name, price, quantity, due_date])
            arquivo_csv.close()

        local_logger.info(f"Produto {new_id} adicionado com sucesso.")

        return {"message": "Produto adicionado com sucesso", "id": new_id}
    except Exception as e:
        local_logger.error(f"Erro ao adicionar produto: {e}")
        return {"message": "Erro ao adicionar produto"}

