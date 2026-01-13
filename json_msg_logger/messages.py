from enum import Enum

from json_msg_logger.config import LogLevels

# class Statuses(Enum):
#   OK = "ok"
#   WARN = "warn"
#   ERROR = "error"

class Message:
  def __init__(self, message: str, level: LogLevels, err: str = "", code_id: int = 0):
    self.message: str = message
    self.err: str = err
    self.code_id: int = code_id
    self.level: LogLevels = level

  def set_message(self, message: str):
    self.message = message

  def set_code_id(self, code_id: int):
    self.code_id = code_id
  
  def set_level(self, level: str):
    self.level = level
  
  def set_error(self, err: str):
    self.err = err

  def get_error(self) -> str:
    return self.err

  def get_message(self) -> str:
    return self.message

  def get_code_id(self) -> int:
    return self.code_id
  
  def get_level(self) -> LogLevels:
    return self.level
  

# class GeneralMessages(Enum):

#   STARTING_APPLICATION = Message(message="Starting RAG application",code_id=10,level=LogLevels.INFO,status=Statuses.OK)

#   INITIALIZE_LLMS_SUCCESS = Message(message="Initialize LLMs models",code_id=100,level=LogLevels.DEBUG, status=Statuses.OK)
#   INITIALIZE_VECTOR_STORE_SUCCESS = Message(message="Vector store initialized with success",code_id=110,level=LogLevels.DEBUG, status=Statuses.OK)
#   INITIALIZE_CHAT_HISTORY_SUCCESS = Message(message="Chat history initialized with success",code_id=120,level=LogLevels.DEBUG, status=Statuses.OK)

#   SETTING_CACHE_CONFIG_SUCCESS = Message(message="Setting the cache config with success",code_id=200,level=LogLevels.DEBUG, status=Statuses.OK)
#   SETTING_VECTOR_STORE_CONFIG_SUCCESS = Message(message="Setting the vector store config with success",code_id=210,level=LogLevels.TRACE, status=Statuses.OK)
#   SETTING_CHAT_HISTORY_CONFIG_SUCCESS = Message(message="Setting the chat history config with success",code_id=220,level=LogLevels.DEBUG, status=Statuses.OK)

#   CREATING_CHAINS_SUCCESS = Message(message="Creating chains with success",code_id=300,level=LogLevels.DEBUG, status=Statuses.OK)

#   RETRIEVE_DOCUMENTS_SUCCESS = Message(message="Documents retrieved from vector store with success",code_id=1000,level=LogLevels.WARN, status=Statuses.OK)
#   RETRIEVE_DOCUMENTS_EMPTY = Message(message="No documents found in vector store",code_id=1001,level=LogLevels.DEBUG, status="warn")
#   RETRIEVE_DOCUMENTS_FROM_CACHE_SUCCESS = Message(message="Documents retrieved from cache with success",code_id=1002,level=LogLevels.DEBUG, status=Statuses.OK)
#   STORE_DOCUMENTS_SUCCESS = Message(message="Documents stored in vector store with success",code_id=1010,level=LogLevels.DEBUG, status=Statuses.OK)
#   STORE_DOCUMENTS_INTO_CACHE_SUCCESS = Message(message="Documents stored in cache with success",code_id=1011,level=LogLevels.DEBUG, status=Statuses.OK)

#   LOAD_DOCUMENTS_SUCCESS = Message(message="Documents loaded with success",code_id=3000,level=LogLevels.DEBUG, status=Statuses.OK)
#   CHUNK_DOCUMENTS_SUCCESS = Message(message="Documents chunked with success",code_id=3100,level=LogLevels.DEBUG, status=Statuses.OK)

#   PROCESSING_QUESTION_SUCCESS = Message(message="Question processed with success",code_id=2000,level=LogLevels.INFO, status=Statuses.OK)
#   ANSWER_QUESTION_SUCCESS = Message(message="Answer generated with success",code_id=2100,level=LogLevels.INFO, status=Statuses.OK)
#   ANSWER_FROM_CACHE_SUCCESS = Message(message="Answer retrieved from cache with success",code_id=2110,level=LogLevels.INFO, status=Statuses.OK)
#   RETURNING_ANSWER_SUCCESS = Message(message="Answer returned with success",code_id=2900,level=LogLevels.INFO, status=Statuses.OK)

#   SERVICER_THREADS_STARTED = Message(message="Servicer thread started",code_id=4000,level=LogLevels.TRACE, status=Statuses.OK)
#   SERVICER_THREADS_STOPPING = Message(message="Stopping servicer thread",code_id=4100,level=LogLevels.TRACE, status=Statuses.OK)
#   SERVICER_THREADS_STOPPED = Message(message="Servicer thread stopped",code_id=4101,level=LogLevels.TRACE, status=Statuses.OK)
#   SERVICER_THREAD_REGAINING = Message(message="Attempting to regain servicer thread.",code_id=4200,level=LogLevels.TRACE, status=Statuses.OK)
#   SERVICER_THREADS_COMPLETED = Message(message="Servicer thread completed successfully.",code_id=4300,level=LogLevels.TRACE, status=Statuses.OK)

# class ErrorMessages(Enum):

#   KEYBOARD_INTERRUPT = Message(message="Keyboard interrupt detected, shutting down gracefully.",code_id=100, level=LogLevels.ERROR, status=Statuses.ERROR)

#   RPC_CANCELLED_FROM_CLIENT = Message(message="RPC cancelled from client.",code_id=1000,level=LogLevels.WARN, status=Statuses.ERROR)

#   COLLECTION_NOT_FOUND = Message(message="Collection in vector store not found",code_id=2000,level=LogLevels.ERROR, status=Statuses.ERROR)
#   DOCUMENTS_NOT_FOUND = Message(message="No documents found in vector store.",code_id=2200,level=LogLevels.WARN, status=Statuses.ERROR)
#   RETRIEVE_DOCUMENTS = Message(message="Error to retrieve data from vector store.",code_id=2210,level=LogLevels.ERROR, status=Statuses.ERROR)

#   INITIALIZE_EMBEDDINGS = Message(message="Error to initialize the embeddings model.",code_id=3000,level=LogLevels.ERROR, status=Statuses.ERROR)
#   INITIALIZE_LLMS = Message(message="Error to initialize the LLM model.",code_id=3010,level=LogLevels.ERROR, status=Statuses.ERROR)

#   LOAD_FILES = Message(message="Error to load files.",code_id=4000,level=LogLevels.ERROR, status=Statuses.ERROR)

#   PROCESSING_QUESTION = Message(message="Error to process the question.",code_id=6000,level=LogLevels.ERROR, status=Statuses.ERROR)

#   SOME_ERROR_OCURRED = Message(message="Some error ocurred.",code_id=9000,level=LogLevels.ERROR, status=Statuses.ERROR)
