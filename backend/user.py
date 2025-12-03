from dataclasses import dataclass
import bcrypt

@dataclass
class User:
    username: str
    password_hash: str

    @staticmethod
    def hash_password(password):
        if isinstance(password, bytes):
            password = password.decode()
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    
    def authenticate(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())