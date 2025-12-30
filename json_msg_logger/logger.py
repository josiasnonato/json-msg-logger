import logging

import json_msg_logger.messages as messages_module
import json_msg_logger.messages as logging_config_module

class Logger():

  def __init__(self):
    self.extra: dict = {}
    self.message: messages_module.Message = None
    self.level: logging.Logger = logging.INFO
    self.logger = logging.getLogger(__name__.split(".")[0])

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
  
  def get_message(self) -> logging_config_module.Message:
    return self.message

  def get_extra(self) -> dict:
    if self.extra is None:
      return {}
    return self.extra
  
  def get_error(self) -> str:
    return self.err
  
  def log(self, message: logging_config_module.Message, level: logging_config_module.LogLevels = logging_config_module.LogLevels.INFO, extra: dict = {}):

    self.message = message
    self.level = level

    if extra:
      self.extra.update(extra)

    if self.message.get_code_id() != 0:
      self.extra.update({"code_id": self.message.get_code_id()})

    self._log()
    
    for key in extra.keys():
      self.extra.pop(key)

  def _log(self):
    try:
      self.logger.log(level=self.level, msg=self.message.get_message(), extra={"extra": self.get_extra()}, stacklevel=2)
    except Exception as e:
      self.logger.error(f"Logging failed: {str(e)}")

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
