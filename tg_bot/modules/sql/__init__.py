from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from tg_bot import DB_URI

BASE = declarative_base()
_engine = create_engine(DB_URI)
SESSION = scoped_session(sessionmaker(bind=_engine, autoflush=False))

# Import all model modules to register ORM classes with BASE,
# then create all tables before any data-loading calls run.
# Each *_sql module must import BASE/SESSION at top, define its models,
# then call create_tables() before running any queries.

def create_tables():
    BASE.metadata.create_all(_engine)
