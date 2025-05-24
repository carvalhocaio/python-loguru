"""
Usar o decorador básico @logger.catch é uma boa ideia porque não requer configuração e captura
todas as exceções automaticamente. No entanto, em aplicações maiores, muitas vezes você precisa
de mais controle sobre como os erros são registrados e tratados. Você pode querer personalizar
a mensagem de erro, definir níveis de log específicos ou tratar certos tipos de erros de maneira
diferente. Para resolver isso, você pode personalizar o decorador @logger.catch com parâmetros
adicionais.
"""

from loguru import logger


@logger.catch(message="database connection failed", level="ERROR")
def connect_to_db(host, port):
    if port < 1_000:
        raise ValueError("Invalid port number")

    # simulated database connection
    return 1 / 0  # simulate error


connect_to_db("localhost", 123)
