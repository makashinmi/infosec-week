from dotenv import load_dotenv
from os import environ as env

load_dotenv()


class Config:
    DB_USER = env.get('DB_USER')
    DB_PASSWORD = env.get('DB_PASSWORD')
    DB_ADDRESS = env.get('DB_ADDRESS')
    DB_PORT = env.get('DB_PORT')
    DB_NAME = env.get('DB_NAME')

    def getDatabaseURI(self):
        return f'{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_ADDRESS}:{self.DB_PORT}/{self.DB_NAME}'


cfg = Config()

