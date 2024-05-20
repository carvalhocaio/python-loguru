from loguru import logger

fmt = "{time} - {name} - {level} - {message}"

logger.add("compressed.log", format=fmt, level="DEBUG", rotation="50 B", compression="zip")
logger.debug("This is a debug message")
logger.info("This is a informational message")

for i in range(2):
    logger.info(f"Log message {i}")
