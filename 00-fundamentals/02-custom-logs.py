"""
Embora a configuração padrão do Loguru seja útil imediatamente, muitas vezes você vai querer
personalizar como seus logs aparecem e quais mensagens são registradas. O Loguru torna essa
personalização simples através do método .add() com o parâmetro format.
"""

import sys
from loguru import logger

logger.remove()
logger.add(sys.stderr, format="{message}")

logger.info("A minimal log message")
