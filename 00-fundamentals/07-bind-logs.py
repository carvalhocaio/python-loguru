"""
O método .bind() é útil quando você deseja anexar informações persistentes a cada mensagem de log
de uma instância específica do logger, como IDs de usuário, IDs de sessão ou informações do
servidor. Isso evita que você precise incluir manualmente essas informações em cada mensagem de
log e garante consistência em todos os logs desse logger em particular.
"""

import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr, format="{time} | {level} | {message} | {extra}")

user_logger = logger.bind(user_id=123)
user_logger.info("user logged in")
user_logger.info("user started a session")
