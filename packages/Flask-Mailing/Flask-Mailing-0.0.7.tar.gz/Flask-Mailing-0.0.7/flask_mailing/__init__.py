from .mail import Mail
from .config import  ConnectionConfig
from .schemas import (
    Message as Message, 
    MultipartSubtypeEnum as MultipartSubtypeEnum
    )
from . import utils


version_info = (0, 0, 6)

__version__ = ".".join([str(v) for v in version_info])


__author__ = "aniketsarkar@yahoo.com"



__all__ = [
    "Mail", "ConnectionConfig", "Message", "utils", "MultipartSubtypeEnum"
]