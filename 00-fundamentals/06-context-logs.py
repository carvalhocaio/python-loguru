"""
Frequentemente, você vai querer incluir contexto extra em suas mensagens de log para ajudar a
entender melhor o que estava acontecendo quando o log foi criado. O Loguru fornece várias
maneiras de adicionar esse contexto. A abordagem mais simples é passar argumentos nomeados
diretamente para seus métodos de logging.
"""

import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr, format="{time} | {level} | {message} | {extra}")

logger.info("User logged in", user_id=123)
