"""
Ao trabalhar com aplicações maiores, você frequentemente precisa de identificadores
permanentes — como IDs de usuário — e temporários, como IDs de requisição ou transação. Ao
combinar .bind() e .contextualize(), você pode construir um panorama completo do que está
acontecendo em sua aplicação.
"""

import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr, format="{time} | {level} | {message} | {extra}")

user_logger = logger.bind(user_id=123)
with user_logger.contextualize(request_id="abc789"):
    user_logger.info("processing user request")

user_logger.info("another user action unrelated to previous request.")
