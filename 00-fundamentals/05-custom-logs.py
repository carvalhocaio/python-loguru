"""
O Loguru também suporta marcação de cores em suas strings de formatação. Você pode usar tags
como <red>, <green>, <blue> e outras, e elas serão automaticamente convertidas em cores no terminal.
"""

import sys
from loguru import logger

logger.info("Database connection established - without custom")

logger.remove()
logger.add(
    sys.stderr,
    format=(
        "[<red>{time:HH:mm:ss}</red>] >> "
        "<yellow>{level}</yellow>: "
        "<cyan>{message}</cyan>"
    ),
)

logger.info("Database connection established")
