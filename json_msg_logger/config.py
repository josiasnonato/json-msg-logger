import logging
import json

TRACE_LEVEL = 1

class JsonFormatter(logging.Formatter):
  def __init__(self, app_name: str, datefmt: str):
    super().__init__(datefmt=datefmt)
    self.app_name = app_name

  def format(self, record):
    log_record = {
      "app_name": self.app_name,
      "timestamp": self.formatTime(record, self.datefmt),
      "level": record.levelname,
      "message": record.getMessage(),
      "pathname": record.pathname+":"+str(record.lineno),
    }

    if hasattr(record, 'extra'):
      log_record.update(record.extra)

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
  logger = logging.getLogger(__name__.split(".")[0])
  logger.setLevel(logging._nameToLevel.get(log_level.upper()))
  if logger.handlers:
    logger.handlers[0].setLevel(logging._nameToLevel.get(log_level.upper()))

app_name: str = __name__.split(".")[0]

logging.addLevelName(TRACE_LEVEL, "TRACE")
logger = logging.getLogger(__name__.split(".")[0])
logger.setLevel(logging._nameToLevel.get("INFO"))

# Avoid adding duplicate handlers
if not logger.handlers:
  handler = logging.StreamHandler()

  formatter = JsonFormatter(app_name=app_name, datefmt="%Y-%m-%dT%H:%M:%S")
  handler.setFormatter(formatter)

  logger.addHandler(handler)
  logger.propagate = False
