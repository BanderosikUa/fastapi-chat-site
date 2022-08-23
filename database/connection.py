from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from core.settings import DB_NAME, DB_USER_PASSWORD, DB_USER_USERNAME

engine = create_engine(
    "mariadb+mariadbconnector:"
    f"//{DB_USER_USERNAME}:{DB_USER_PASSWORD}@127.0.0.1:3306/{DB_NAME}"
   )

Session = sessionmaker(bind=engine)

Base = declarative_base()


class DbContext:
    def __init__(self):
        self.db = Session()

    def __enter__(self):
        return self.db

    def __exit__(self, et, ev, traceback):
        self.db.close()