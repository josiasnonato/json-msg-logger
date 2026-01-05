import logging

import json_msg_logger.messages as messages_module
import json_msg_logger.messages as logging_config_module
from json_msg_logger.config import logger

class Logger():

  def __init__(self, app_name: str = ""):
    self.extra: dict = {}
    self.message: messages_module.Message = None
    self.level: logging.Logger = logging.INFO
    self.depth: int = 1
    self.app_name: str = app_name

  def clear(self):
    self.extra.clear()
    self.level = None
    self.message = None
    
  def trace(self):
    self.message.level = logging_config_module.LogLevels.TRACE

  def debug(self):
    self.message.level = logging_config_module.LogLevels.DEBUG

  def info(self):
    self.message.level = logging_config_module.LogLevels.INFO

  def warning(self):
    self.message.level = logging_config_module.LogLevels.WARN

  def error(self):
    self.message.level = logging_config_module.LogLevels.ERROR

  def critical(self):
    self.message.level = logging_config_module.LogLevels.CRITICAL

  def set_message(self, message: logging_config_module.Message):
    self.message = message

  def set_error(self, err: str):
    self.err = err

  def set_extra(self, extra: dict):
    self.extra = extra
  
  def set_depth(self, depth: int):
    self.depth = depth
  
  def set_app_name(self, app_name: str):
    self.app_name = app_name
  
  def get_message(self) -> logging_config_module.Message:
    return self.message

  def get_extra(self) -> dict:
    if self.extra is None:
      return {}
    return self.extra
  
  def get_error(self) -> str:
    return self.err

  def get_depth(self) -> int:
    return self.depth

  def get_app_name(self) -> str:
    return self.app_name
  
  def log(self, message: logging_config_module.Message, level: logging_config_module.LogLevels = None, extra: dict = {}, depth: int = 1):

    self.message = message

    if level:
      self.level = level
    else:
      self.level = self.message.get_level()

    if extra:
      self.extra.update(extra)

    if self.message.get_code_id() != 0:
      self.extra.update({"code_id": self.message.get_code_id()})

    if self.depth < 0:
      self.depth = 2
    else:
      self.depth = depth + 2
    
    self._log()
    
    for key in extra.keys():
      self.extra.pop(key)

  def _log(self):
    
    if self.app_name != "":
      self.extra.update({"app_name": self.app_name})

    try:
      logger.log(level=self.level, msg=self.message.get_message(), extra={"extra": self.get_extra()}, stacklevel=self.get_depth())
    except Exception as e:
      logger.error(f"Logging failed: {str(e)}")

# Example to print a log with simple message
# LoggerMessages(message=GeneralMessages.RETRIEVE_DOCUMENTS_SUCCESS.value).print()
#
# Custom message without context, but with error and extra data
# LoggerMessages(message=GeneralMessages.RETRIEVE_DOCUMENTS_SUCCESS.value, err="some error", extra={"test": 1}).print()
#
# Context can be passed from gRPC ServicerContext and the metadata will be extracted automatically
# LoggerMessages(message=GeneralMessages.RETRIEVE_DOCUMENTS_SUCCESS.value, context=context, extra={"test": 2}).print()
#
# Different examples of usage:
# LoggerMessages(message=GeneralMessages.RETRIEVE_DOCUMENTS_SUCCESS.value, context=context, err="some err again", extra={"any_info": "information"}).print()
# LoggerMessages(message=GeneralMessages.RETRIEVE_DOCUMENTS_SUCCESS.value, context=context).print()
# LoggerMessages(message=GeneralMessages.RETRIEVE_DOCUMENTS_SUCCESS.value, err="some error").print()
# LoggerMessages(message=GeneralMessages.RETRIEVE_DOCUMENTS_SUCCESS.value, extra={"any_data":"email@email.com"}).print()
#
# Custom message
# LoggerMessages(message=Message("Custom message here", level=LogLevels.INFO, code_id=500), context=context, extra={"test": "true"}).print()
