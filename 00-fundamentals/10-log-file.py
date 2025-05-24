from loguru import logger

logger.add("app.log")
logger.info("this a message goes to app.log")
