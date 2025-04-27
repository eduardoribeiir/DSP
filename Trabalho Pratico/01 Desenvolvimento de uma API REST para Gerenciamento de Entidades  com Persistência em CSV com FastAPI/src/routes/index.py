from src.local_logger import local_logger

async def index():
    local_logger.info(f'Rota inicial acessada')

    return {"message": "World"}