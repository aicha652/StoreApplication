from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


if getenv("ECOMM_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
