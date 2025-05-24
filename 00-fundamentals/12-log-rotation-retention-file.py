"""
O parâmetro rotation define quando iniciar um novo arquivo de log. Ele aceita vários tipos de
argumentos diferentes:

- Baseado em tamanho: Cria um novo arquivo quando o tamanho atinge um limite ("100 MB", "2 GB").
- Baseado em tempo: Cria um novo arquivo em horários específicos ("00:00" para diariamente).
- Baseado em intervalo: Cria um novo arquivo após durações definidas ("12 hours", "3 days").

Mas o que acontece com esses arquivos rotacionados? Por padrão, eles se acumulam
indefinidamente, o que consome espaço em disco. O recurso de retenção do Loguru ajuda a
gerenciar isso limpando automaticamente os arquivos de log antigos.
"""

import time
from loguru import logger

logger.add("app.log", rotation="5 seconds", retention="1 minute")

for i in range(100):
    logger.info(f"processing item #{i}")
    time.sleep(2)
