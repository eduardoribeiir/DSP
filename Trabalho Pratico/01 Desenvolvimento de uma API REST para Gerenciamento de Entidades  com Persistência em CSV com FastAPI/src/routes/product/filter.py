import csv
from datetime import date, datetime
from src.local_logger import local_logger
from src.models.Product import Product

async def get_products() -> list[Product]:
    try:
        rows = []
        
        with open('database/produtos.csv', 'r') as arquivo_csv:
            reader_arquivo = csv.reader(arquivo_csv)
            next(reader_arquivo)
            rows = list(reader_arquivo)
            arquivo_csv.close()

        if not rows:
            local_logger.info("Nenhum produto encontrado.")
            return []

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

        local_logger.info("Produtos encontrados com sucesso.")
        return products
    except Exception as e:
        local_logger.error(f"Nenhum produto encontrado: {e}")
        return []
    
async def filter_product_by_price(min_price: float, max_price: float):
    try:
        all_products = await get_products()

        filtered_products = []
        for product in all_products:
            if product.price >= min_price and product.price <= max_price:
                filtered_products.append(product)

        local_logger.info("Produtos filtrados com sucesso.")
        return filtered_products
    except Exception as e:
        local_logger.error(f"Erro ao filtrar produtos: {e}")
        return {"message": "Erro ao filtrar produtos"}

async def filter_product_by_due_date(ini_due_date_str: str, final_due_date_str: str):
    try:
        all_products = await get_products()

        date_format = "%Y-%m-%d"
        ini_due_date = datetime.strptime(ini_due_date_str, date_format)
        final_due_date = datetime.strptime(final_due_date_str, date_format)

        filtered_products = []
        for product in all_products:
            product_due_date = datetime.strptime(product.due_date, date_format)
            if product_due_date >= ini_due_date and product_due_date <= final_due_date:
                filtered_products.append(product)

        local_logger.info("Produtos filtrados com sucesso.")
        return filtered_products
    except Exception as e:
        local_logger.error(f"Erro ao filtrar produtos: {e}")
        return {"message": "Erro ao filtrar produtos"}