import logging
import json

TRACE_LEVEL = 1
LOGGER_NAME: str = __name__.split(".")[0]
APP_NAME: str = ""

class JsonFormatter(logging.Formatter):
  def __init__(self, logger_name: str, datefmt: str):
    super().__init__(datefmt=datefmt)
    self.logger_name = logger_name

  def format(self, record):
    log_record = {
      "logger": self.logger_name,
      "timestamp": self.formatTime(record, self.datefmt),
      "level": record.levelname,
      "message": record.getMessage(),
      "pathname": record.pathname+":"+str(record.lineno),
    }

    if hasattr(record, 'extra'):
      log_record.update(record.extra)
    
    if APP_NAME != "":
      log_record["app_name"] = APP_NAME

    return json.dumps(log_record)

class LogLevels(logging.Logger):

  TRACE = TRACE_LEVEL          # TRACE: print message showing data generally. Useful to trace program execution or data flow
  DEBUG = logging.DEBUG        # DEBUG: print message useful for debugging, showing detailed information
  INFO = logging.INFO          # INFO: print message showing general information about program execution
  WARN = logging.WARN          # WARN: print message showing a warning about a potential issue
  ERROR = logging.ERROR        # ERROR: print message showing an error that occurred during program execution
  CRITICAL = logging.CRITICAL  # CRITICAL: print message showing a critical error that may cause program termination

  def trace(self, msg, *args, **kwargs):
    self.log(self.TRACE, msg, *args, **kwargs)

def set_logger_level(log_level: str) -> None:
  logger = logging.getLogger(LOGGER_NAME)
  logger.setLevel(logging._nameToLevel.get(log_level.upper()))
  if logger.handlers:
    logger.handlers[0].setLevel(logging._nameToLevel.get(log_level.upper()))

def set_app_name(app_name: str) -> None:
  global APP_NAME
  APP_NAME = app_name

logging.addLevelName(TRACE_LEVEL, "TRACE")
logger = logging.getLogger(APP_NAME)
logger.setLevel(logging._nameToLevel.get("DEBUG"))
# logger.addFilter(logging.Filter(name=LOGGER_NAME))
# logger.name = APP_NAME

# Avoid adding duplicate handlers
if not logger.handlers:
  handler = logging.StreamHandler()

  formatter = JsonFormatter(logger_name=LOGGER_NAME, datefmt="%Y-%m-%dT%H:%M:%S")
  handler.setFormatter(formatter)

  logger.addHandler(handler)
  logger.propagate = False
