from pytest_factoryboy import register

from models import Customer, Employee, CustomerType
from crud import get_session, get_customers
from tests.factories import EmployeeFactory, TeamFactory

session = get_session()


def test_get_customers():
    employee = Employee(name='Jane Smith', sesa='SESA111')
    customer_type = CustomerType(name='Typ 1', zone='A', priority=1)
    session.add(employee, customer_type)
    session.flush()
    for name in ['ABC', 'HM']:
        customer = Customer(name=name, employee=employee, customer_type=customer_type)
    result = get_customers(session, sesa='SESA111', customer_type='Typ 1')
    assert len(result) == 2


def test_get_customers_realistic():
    # more employees, customer types
    pass


def test_get_customers_from_team(employee_factory, team_factory):
    pass
