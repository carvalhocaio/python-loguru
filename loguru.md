# Entendendo os Níveis de Log

Vamos explorar os níveis de log do Loguru em mais detalhes. Os níveis de log permitem categorizar
mensagens conforme sua gravidade e aimportância, facilitando o filtro e o gerenciamento dos logs.

O Loguru oferece sete níveis de log integrados, cada um com seu próprio método, valor de 
severidade e esquema de cores padrão:

| Nível      | Método               | Valor | Finalidade                                                                |
|------------|----------------------|-------|---------------------------------------------------------------------------|
| TRACE      | `logger.trace()`     | 5     | Informações extremamente detalhadas para depuração                        |
| DEBUG      | `logger.debug()`     | 10    | Informações úteis durante o desenvolvimento                               |
| INFO       | `logger.info()`      | 20    | Informações gerais sobre o que está acontecendo no código                 |
| SUCCESS    | `logger.success()`   | 25    | Notificações de operações bem-sucedidas                                   |
| WARNING    | `logger.warning()`   | 30    | Avisos sobre algo inesperado, mas não necessariamente problemático        |
| ERROR      | `logger.error()`     | 40    | Erros quando algo falha, mas a aplicação continua rodando                 |
| CRITICAL   | `logger.critical()`  | 50    | Erros críticos que são sérios e urgentes                                  |


# Registro em Arquivos Usando o Loguru

Embora o registro no console seja útil durante o desenvolvimento, na produção, normalmente você
desejará gravar registros em arquivos. O Loguru permite a configuração do registro em arquivos
com recursos avançados, como rotação de registros e políticas de retenção.

Antes de analisar os exemplos de implementação, você precisa entender as duas principais políticas
de gerenciamento que o Loguru oferece para organizar seus arquivos de log de forma organizada:

- **Rotação de log**: determina quando iniciar um novo arquivo de log, com base no tamanho do
arquivo, intervalos de tempo ou outras condições.

- **Retenção de log**: controla por quanto tempo os arquivos de log antigos devem ser mantidos
antes de serem excluídos, com base na contagem ou na idade dos arquivos.
