import csv
from src.local_logger import local_logger
from src.models.Product import Product

async def read_product():
    try:
        rows = []
        
        with open('database/produtos.csv', 'r') as arquivo_csv:
            reader_arquivo = csv.reader(arquivo_csv)
            next(reader_arquivo)
            rows = list(reader_arquivo)
            arquivo_csv.close()

        if not rows:
            local_logger.info("Nenhum produto encontrado.")
            return {"message": "Nenhum produto encontrado"}

        products = []
        for row in rows:
            product = Product(
                id=int(row[0]),
                name=row[1],
                price=float(row[2]),
                quantity=int(row[3]),
                due_date=row[4]
            )
            products.append(product)

        local_logger.info("Produtos lidos com sucesso.")
        return products
    except Exception as e:
        local_logger.error(f"Erro ao ler produtos: {e}")
        return {"message": "Erro ao ler produtos"}