import logging

logger = logging.getLogger("loger_name")
# output of logger object
logger.debug("Logging at debug") # hidden because below of warning
logger.info("Logging at info") # hidden because below of warning
logger.warning("Logging at warning")
logger.error("Logging at error")
logger.fatal("Logging at fatal")

# include information when logging:
system = "moon"
for num in range(3):
    logger.warning("%d errors reported in %s", num, system)