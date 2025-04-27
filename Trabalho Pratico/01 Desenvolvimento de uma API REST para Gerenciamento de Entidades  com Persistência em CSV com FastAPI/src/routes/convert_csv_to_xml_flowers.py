import os
import pandas as pd
from fastapi.responses import FileResponse
from src.local_logger import local_logger

async def convert_csv_to_xml_flowers():
    try:
        df = pd.read_csv('database/flowers.csv', sep=',', encoding='utf-8')
        # criar pasta exports se não existir
        if not os.path.exists('xmls'):
            os.makedirs('xmls')

        df.to_xml('xmls/flowers.xml', index=False, root_name='flowers', row_name='flower')

        local_logger.info("Conversao de CSV para XML realizada com sucesso.")

        return FileResponse('xmls/flowers.xml', media_type='application/xml', filename='flowers.xml')
    except Exception as e:

        local_logger.error(f"Erro ao converter csv para xml: {e}")
        return {"message": str(e)}

