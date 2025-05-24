"""
A string de formatação suporta vários marcadores de posição que são substituídos por valores reais:

{time}: Data e hora
{level}: Nível do log
{message}: A mensagem real do log
{name}: Nome do módulo
{line}: Número da linha
"""

import sys
from loguru import logger

logger.info("A more informative log message without custom")

logger.remove()
logger.add(
    sys.stderr, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

logger.info("A more informative log message with custom")
