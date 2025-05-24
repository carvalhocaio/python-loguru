"""
O método .contextualize() oferece uma maneira simples de adicionar contexto temporário que é
automaticamente removido assim que você termina aquela operação.
"""

import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr, format="{time} | {level} | {message} | {extra}")

with logger.contextualize(request_id="abc789"):
    logger.info("processing request")
    logger.info("request completed")

logger.info("request is processed, this will not show extra context.")
