import grpc
import logging

# import askly_store. as config_module

import json_msg_logger.messages as messages_module
import json_msg_logger.messages as logging_config_module
# from askly_store.config.config import global_config

class LoggerMessages():

  def __init__(self, message: messages_module.Message, err: str = "", context: grpc.ServicerContext = None, extra: dict = {}):
    self.context: grpc.ServicerContext = context
    self.message: messages_module.Message = message
    self.extra: dict = extra
    self.err: str = err

  def clear(self):
    self.extra.clear()
    self.err = None
    self.message = None
    self.context = None

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

  def set_context(self, context: grpc.ServicerContext):
    self.context = context

  def set_extra(self, extra: dict):
    self.extra = extra
  
  def get_context(self) -> grpc.ServicerContext:
    return self.context
  
  def get_message(self) -> logging_config_module.Message:
    return self.message

  def get_extra(self) -> dict:
    if self.extra is None:
      return {}
    return self.extra
  
  def get_error(self) -> str:
    return self.err
  
  def print(self):

    if self.context is not None:
      ctx_metadata = dict(self.context.invocation_metadata())

      if "request_id" in ctx_metadata:
        self.extra.update({"request_id": ctx_metadata["request_id"]})
        del ctx_metadata["request_id"]

      self.extra.update({"context": {**ctx_metadata}})

    if self.message.get_code_id() != 0:
      self.extra.update({"code_id": self.message.get_code_id()})

    if self.get_error() != "":
      self.extra.update({"error": self.get_error()})
    
    
    l = logging.getLogger(__name__.split(".")[0])
    l.log(level=self.message.get_level(), msg=self.message.get_message(), extra={"extra": self.get_extra()}, stacklevel=2)
    # Clear self data after print
    self.clear()
    # l.handlers[0].flush()
    

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
