from alembic import command
from alembic.config import Config

import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import database_exists, create_database

from config import cfg
from .user import User


engine = create_engine(f'postgresql://{cfg.getDatabaseURI()}')

if not database_exists(engine.url):
    create_database(engine.url)

# This looks wrong. Research the proper way of handling all this shit using alembic and ORM models
User.__table__.create(engine, checkfirst=True)

# What is this supposed to do? What advantage is supposed to be taken from it?
alembic_cfg = Config(f'{__path__[0]}/../alembic.ini')
alembic_cfg.set_main_option('sqlalchemy.url', str(engine.url))
command.stamp(alembic_cfg, 'head')

