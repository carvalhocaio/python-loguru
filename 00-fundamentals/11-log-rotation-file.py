"""
Você notará que a configuração básica, embora simples, possui algumas limitações: o arquivo
crescerá indefinidamente enquanto sua aplicação estiver em execução. A rotação de logs, que cria
automaticamente novos arquivos de log com base em condições de tamanho ou tempo, resolve esse
problema ao evitar que qualquer arquivo fique grande demais.

Enquanto sua aplicação estiver em execução, você pode controlar quando novos arquivos de log são
criados usando a rotação.
"""

from loguru import logger

logger.add("app.log", rotation="4 KB")

for i in range(100):
    logger.info(f"processind item #{i}")
