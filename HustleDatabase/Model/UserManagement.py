from dataclasses import dataclass
from datetime import datetime

@dataclass
class UserManagement():
    userId: str
    username: str
    password: str
    lastLogin: datetime
    lastLogout: datetime