from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from hashlib import md5


class User(declarative_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False, index=True)
    last_name = Column(String, nullable=False, index=True)
    patronymic = Column(String, nullable=True, index=True)
    email = Column(String, unique=False, nullable=True)
    hashed_password = Column(String, nullable=False)

    def set_password(self, password):
        self.hashed_password = md5(bytes(password, 'utf-8')).hexdigest()

    def check_password(self, password):
        return md5(bytes(password, 'utf-8')).hexdigest() == self.hashed_password
