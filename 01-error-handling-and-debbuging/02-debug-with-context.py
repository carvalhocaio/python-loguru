"""
Em certos cenários, você provavelmente precisará entender não apenas onde um erro ocorreu, mas
também o estado da sua aplicação quando isso aconteceu. Para conseguir isso, você pode combinar
o tratamento de erros e informações contextuais com a ajuda do gerenciador de
contexto .contextualize() que você viu anteriormente. Aqui está um exemplo de como usá-lo para
criar logs de depuração altamente informativos.
"""

import sys
from loguru import logger

logger.remove()
logger.add(
    sys.stderr,
    format="{time} | {level} | {message} | {extra}",
    level="TRACE",
)


@logger.catch
def perform_action(user, action):
    with logger.contextualize(user=user, action=action):
        logger.trace("starting action")
        logger.info("performing action")
        if action not in ["login", "logout"]:
            logger.trace("invalid action detected")
            raise ValueError("invalid action")
        logger.success("action completed")


perform_action("alice", "delete")
