import pytest
import os
from sqlalchemy_utils import create_database, database_exists, drop_database
from sqlalchemy import create_engine
from pytest_factoryboy import register

from models import Base
from crud import get_session
from tests.factories import EmployeeFactory, TeamFactory, TeamMembershipFactory, EmployeeWithTeamFactory


factories = [EmployeeFactory, TeamFactory, TeamMembershipFactory, EmployeeWithTeamFactory]
for factory in factories:
    register(factory)


@pytest.fixture(scope='session', autouse=True)
def test_session():
    db_url = os.getenv('TEST_DB_URL')
    if database_exists(db_url):
        drop_database(db_url)
    create_database(db_url)
    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    print('Database created.')
    session = get_session(db_url)
    for factory in factories:
        factory._meta.sqlalchemy_session = session
    yield session



