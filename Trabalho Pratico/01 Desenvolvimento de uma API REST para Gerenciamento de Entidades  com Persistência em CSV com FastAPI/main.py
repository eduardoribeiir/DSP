from fastapi import FastAPI
from src.local_logger import local_logger
from src.routes.index import index as index_route
from src.routes.convert_csv_to_xml_flowers import convert_csv_to_xml_flowers
from src.routes.get_sha_256 import get_sha_256
from src.routes.zip_csv import zip_csv

app = FastAPI()

@app.get("/")
async def index():
    return await index_route()

@app.get("/download/xml/flowers")
async def convert_csv_to_xml_flowers_route():
    return await convert_csv_to_xml_flowers()

@app.get("/download/zip/flowers")
async def zip_csv_route():
    return await zip_csv()

@app.get("/hash/flowers")
async def get_sha_256_route():
    return await get_sha_256('database/flowers.csv')
