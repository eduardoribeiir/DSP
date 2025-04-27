import os
import pandas as pd
from fastapi.responses import FileResponse
from src.local_logger import local_logger

async def zip_csv():
    try:
        df = pd.read_csv('database/flowers.csv', sep=',', encoding='utf-8')
        compression_opts = dict(method='zip', archive_name='flowers.csv')
        # criar pasta zips se não existir
        if not os.path.exists('zips'):
            os.makedirs('zips')

        df.to_csv('zips/flowers.zip', compression=compression_opts)

        local_logger.info("Conversao de CSV para ZIP realizada com sucesso.")

        return FileResponse('zips/flowers.zip', media_type='application/zip', filename='flowers.zip')
    except Exception as e:
        local_logger.error(f"Erro ao converter csv para zip: {e}")
        return {"message": str(e)}
    