import logging
import logging.handlers
import datetime

log_get = logging.getLogger("timelog")
log_get.setLevel(logging.DEBUG)

tm_logg = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0,0,0,0))
tm_logg.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

mb_logg = logging.FileHandler('log.log')
mb_logg.setLevel(logging.ERROR)
mb_logg.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

log_get.addHandler(tm_logg)
log_get.addHandler(mb_logg)

log_get.debug("debug message")
log_get.info("info message")
log_get.warning("warning message")
log_get.error("error message")
log_get.critical("critical message")