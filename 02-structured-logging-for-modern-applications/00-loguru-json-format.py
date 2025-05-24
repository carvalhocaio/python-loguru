"""
Quando você precisa que seus logs estejam em um formato estruturado, o Loguru permite que
você os exporte como JSON. Isso é particularmente útil quando você está trabalhando com
ferramentas de análise de logs ou quando precisa processar seus logs programaticamente.

Para ter uma primeira impressão de como a formatação JSON funciona nos logs, adicione
um parâmetro serialize ao método .add().
"""

import sys
from loguru import logger

logger.remove()
logger.add(
    sys.stderr,
    serialize=True,
)

logger.info("user logged in", user_id=123)
