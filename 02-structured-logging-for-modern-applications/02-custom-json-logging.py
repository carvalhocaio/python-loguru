"""
O Loguru permite criar funções de serialização personalizadas, o que simplifica a estrutura
padrão do JSON, e você pode controlar exatamente quais campos aparecem nos seus logs. Isso
resulta em uma saída mais legível, uso otimizado de armazenamento e melhor integração com
ferramentas externas de análise.
"""

import json
from loguru import logger


def simple_serializer(record):
    subset = {
        "time": record["time"].timestamp(),
        "level": record["level"].name,
        "message": record["message"],
        "context": record["extra"],  # Inclua qualquer contexto vinculado
    }

    return json.dumps(subset)


def add_serialization(record):
    record["extra"]["json_output"] = simple_serializer(record)


logger.remove()
logger = logger.patch(add_serialization)
logger.add("custom.json", format="{extra[json_output]}")
logger.bind(user="john").info("user logged in")
logger.bind(order_id=12345).info("order processed")
