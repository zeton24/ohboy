import os
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine

from models import Base

if __name__ == '__main__':
    db_url = os.getenv('TEST_DB_URL')
    if not database_exists(db_url):
        create_database(db_url)
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    print('Schema created.')
