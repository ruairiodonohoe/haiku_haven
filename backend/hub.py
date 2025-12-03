from backend.database import Database
from backend.user_service import UserService
from backend.haiku_service import HaikuSevice


class Hub:
    def __init__(self, database):
        #database = Database(config['connection_string'])
        self.user_service = UserService(database)
        self.haiku_service = HaikuSevice(database)