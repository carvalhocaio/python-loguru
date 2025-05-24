"""
O principal atrativo do Loguru é sua simplicidade em comparação com o módulo de logging padrão
do Python. Em vez de várias linhas de configuração, você pode começar a registrar logs
imediatamente com um logger pré-configurado.

Esta seção aborda os fundamentos do Loguru, desde o uso básico até recursos avançados como
formatação personalizada e gerenciamento de arquivos de log.
Você aprenderá a implementar logs de forma eficaz com configuração mínima, mantendo flexibilidade
para personalizar conforme necessário.

A maneira mais simples de usar o Loguru é através do logger já pronto. Diferente do módulo padrão
do Python, que exige configuração explícita, o Loguru está pronto para uso após a importação.
"""

from loguru import logger

if __name__ == "__main__":
    logger.debug("debug message")
    logger.info("info message")
    logger.error("error message")
