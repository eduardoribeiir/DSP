from fastapi import FastAPI
from src.local_logger import local_logger
from src.routes.index import index as index_route
from src.routes.convert_csv_to_xml import convert_csv_to_xml
from src.routes.get_sha_256 import get_sha_256
from src.routes.zip_csv import zip_csv
from src.routes.product.create import create_product
from src.routes.product.delete import delete_product
from src.routes.product.read import read_product
from src.routes.product.update import update_product
from src.routes.product.count import count_products


app = FastAPI()

@app.get("/")
async def index():
    return await index_route()

# Rotas de produtos

@app.post("/product/create")
async def create_product_route(name: str, price: float, quantity: int, due_date: str = None):
    return await create_product(name, price, quantity, due_date)

@app.delete("/product/delete")
async def delete_product_route(id: int):
    return await delete_product(id)

@app.get("/product/read")
async def read_product_route():
    return await read_product()

@app.put("/product/update")
async def update_product_route(id: int, name: str, price: float, quantity: int, due_date: str):
    return await update_product(id, name, price, quantity, due_date)

@app.get("/product/count")
async def count_product_route():
    return await count_products()

@app.get("/download/xml/products")
async def download_xml_products_route():
    return await convert_csv_to_xml("produtos")

@app.get("/download/zip/products")
async def download_zip_products_route():
    return await zip_csv("produtos")

@app.get("/hash/products")
async def hash_product_route():
    return await get_sha_256('database/produtos.csv')

# Fim - Rotas de produtos