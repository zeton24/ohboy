import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Employee, Customer, CustomerType, TeamMembership, Team


def get_session(db_url=None):
    if not db_url:
        db_url = os.getenv('TEST_DB_URL')
    engine = create_engine(db_url)
    with Session(engine) as session:
        return session


def get_customers(session, sesa: str, customer_type: str):
    return session.query(Customer).join(Employee, CustomerType).filter(
        Employee.sesa == sesa, CustomerType.name == customer_type).all()


def get_customers_from_team(session, team_name: str):
    return session.query(Customer).join(Employee, TeamMembership, Team).filter(Team.name == team_name).all()
