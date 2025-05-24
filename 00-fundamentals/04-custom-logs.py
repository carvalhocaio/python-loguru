"""
Para ajudar na depuração, você pode querer incluir o nome do módulo e o número da linha para ver
exatamente de onde uma mensagem de log se originou.
"""

import sys
from loguru import logger

logger.info("Database connection established - without custom")

logger.remove()
logger.add(
    sys.stderr,
    format="[{time:HH:mm:ss}] >> {name}:{line} >> {level}: {message}",
)

logger.info("Database connection established")
