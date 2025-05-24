"""
Você pode usar um arquivo como saída para seus logs, assim como fez anteriormente. Desta vez, o
arquivo de log será preenchido com um objeto JSON por linha, para que você possa processá-lo com
ferramentas padrão de análise JSON, como o jq.
"""

from loguru import logger

logger.remove()
logger.add("app.json", serialize=True, format="{time} - {level} - {message}")

logger.info("application started")
logger.warning("memory usage high")
