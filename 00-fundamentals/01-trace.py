"""
Por padrão, o Loguru exibe todas as mensagens com nível DEBUG (10) e superiores. Isso significa
que, ao começar a usar o Loguru, você verá a maioria das mensagens de log, exceto as mensagens
extremamente detalhadas de nível TRACE. Esse comportamento ajuda a manter seus logs focados nas
informações mais relevantes durante o desenvolvimento, filtrando detalhes excessivos.
"""

import sys
from loguru import logger


logger.remove()  # this is necessary for not duplicate the logger message
logger.add(sys.stderr, level="TRACE")
logger.trace("will this be visible?")

logger.debug("a debug message")
logger.info("a info message")
