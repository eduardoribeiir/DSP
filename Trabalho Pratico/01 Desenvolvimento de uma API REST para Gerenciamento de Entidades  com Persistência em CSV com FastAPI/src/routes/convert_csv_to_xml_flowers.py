import os
import pandas as pd
from fastapi.responses import FileResponse
from src.local_logger import local_logger

async def convert_csv_to_xml_flowers():
    try:
        df = pd.read_csv('database/flowers.csv', sep=',', encoding='utf-8')

        if not os.path.exists('xmls'):
            os.makedirs('xmls')

        timestamp = pd.Timestamp.now().strftime('%Y%m%d%H%M%S')
        fileName = f"flowers_{timestamp}.xml"

        df.to_xml(f"xmls/{fileName}", index=False, root_name='flowers', row_name='flower')

        local_logger.info("Conversao de CSV para XML realizada com sucesso.")

        return FileResponse(f"xmls/{fileName}", media_type='application/xml', filename=fileName)
    except Exception as e:

        local_logger.error(f"Erro ao converter csv para xml: {e}")
        return {"message": str(e)}

