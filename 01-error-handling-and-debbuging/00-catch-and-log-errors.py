"""
Usando o Decorador @logger.catch

A maneira mais simples de capturar e registrar erros é com o decorador @logger.catch do
Loguru. Ele é especialmente útil quando você quer garantir que quaisquer erros em sua aplicação
sejam automaticamente registrados assim que ocorrerem.
"""

from loguru import logger


@logger.catch
def divide(a, b):
    return a / b


divide(10, 0)
