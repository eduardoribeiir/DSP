import os
import pandas as pd
from fastapi.responses import FileResponse
from src.local_logger import local_logger

async def convert_csv_to_xml(database_name: str):
    try:
        df = pd.read_csv(f"database/{database_name}.csv", sep=',', encoding='utf-8')

        if not os.path.exists('xmls'):
            os.makedirs('xmls')

        timestamp = pd.Timestamp.now().strftime('%Y%m%d%H%M%S')
        fileName = f"{database_name}_{timestamp}.xml"

        df.to_xml(f"xmls/{fileName}", index=False, root_name=database_name, row_name=database_name[:-1])

        local_logger.info(f"Conversao dos/das {database_name} de CSV para XML realizada com sucesso.")

        return FileResponse(f"xmls/{fileName}", media_type='application/xml', filename=fileName)
    except Exception as e:

        local_logger.error(f"Erro ao converter os/as {database_name} de csv para xml: {e}")
        return {"message": "Erro ao criar o arquivo xml"}

