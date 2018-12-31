import logging

Log_format = "%(asctime)s====%(levelname)s====%(message)s"
logging.basicConfig(filename="log.log",level=logging.DEBUG,format=Log_format)

logging.debug("This is a debug log")
logging.info("This i a info log")
logging.warning("This is a Warning log")
logging.error("This is a error log")
logging.critical("This is a critical log")



logging.log(logging.DEBUG,"This is a debug log")
logging.log(logging.INFO,"This is a info log")
logging.log(logging.WARNING,"This is a warning log")
logging.log(logging.ERROR,"This is a error log")
logging.log(logging.CRITICAL,"This is a critical log")
