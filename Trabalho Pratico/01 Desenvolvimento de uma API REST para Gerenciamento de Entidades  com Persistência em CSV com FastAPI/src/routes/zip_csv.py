import os
import pandas as pd
from fastapi.responses import FileResponse
from src.local_logger import local_logger

async def zip_csv(database_name: str):
    try:
        df = pd.read_csv(f"database/{database_name}.csv", sep=',', encoding='utf-8')
        compression_opts = dict(method='zip', archive_name=f"{database_name}.csv")
        if not os.path.exists('zips'):
            os.makedirs('zips')

        timestamp = pd.Timestamp.now().strftime('%Y%m%d%H%M%S')

        fileName = f"{database_name}_{timestamp}.zip"

        df.to_csv(f"zips/{fileName}", compression=compression_opts)

        local_logger.info(f"Conversao dos/das {database_name} de CSV para ZIP realizada com sucesso.")

        return FileResponse(f"zips/{fileName}", media_type='application/zip', filename=fileName)
    except Exception as e:
        local_logger.error(f"Erro ao converter os/as {database_name} de csv para zip: {e}")
        return {"message": "Erro ao criar o arquivo zip"}
    