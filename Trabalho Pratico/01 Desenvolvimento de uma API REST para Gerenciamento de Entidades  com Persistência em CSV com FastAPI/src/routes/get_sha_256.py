import hashlib
from src.local_logger import local_logger

async def get_sha_256(file_path: str):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            sha256_hash = hashlib.sha256(content.encode()).hexdigest()
            return {"message": "Hash gerado com sucesso.", "hash_sha256": sha256_hash}
    except Exception as e:
        local_logger.error(f"Erro ao gerar hash SHA-256: {e}")
        return {"message": str(e)}