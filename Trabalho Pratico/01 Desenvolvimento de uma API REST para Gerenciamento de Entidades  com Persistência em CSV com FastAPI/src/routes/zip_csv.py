import os
import pandas as pd
from fastapi.responses import FileResponse
from src.local_logger import local_logger

async def zip_csv():
    try:
        df = pd.read_csv('database/flowers.csv', sep=',', encoding='utf-8')
        compression_opts = dict(method='zip', archive_name='flowers.csv')
        if not os.path.exists('zips'):
            os.makedirs('zips')

        timestamp = pd.Timestamp.now().strftime('%Y%m%d%H%M%S')

        fileName = f"flowers_{timestamp}.zip"

        df.to_csv(f"zips/{fileName}", compression=compression_opts)

        local_logger.info("Conversao de CSV para ZIP realizada com sucesso.")

        return FileResponse(f"zips/{fileName}", media_type='application/zip', filename=fileName)
    except Exception as e:
        local_logger.error(f"Erro ao converter csv para zip: {e}")
        return {"message": str(e)}
    