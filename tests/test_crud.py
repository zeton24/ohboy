from models import Customer, Employee, CustomerType
from crud import get_customers, get_employees_from_team


def test_get_customers(test_session):
    employee = Employee(name='Jane Smith', sesa='SESA111')
    customer_type = CustomerType(name='Typ 1', zone='A', priority=1)
    test_session.add(employee, customer_type)
    for name in ['ABC', 'HM']:
        customer = Customer(name=name, employee=employee, customer_type=customer_type)
    result = get_customers(test_session, sesa='SESA111', customer_type='Typ 1')
    assert len(result) == 2


def test_get_customers_with_factories(test_session, customer_factory):
    customer = customer_factory.create()
    result = get_customers(test_session, sesa=customer.employee.sesa, customer_type=customer.customer_type.name)
    customer_factory.create_batch(5)
    assert len(result) == 1
    assert result[0].name == customer.name
    customer_factory.create_batch(3, employee=customer.employee, customer_type=customer.customer_type)
    result2 = get_customers(test_session, sesa=customer.employee.sesa, customer_type=customer.customer_type.name)
    assert len(result2) == 4


def test_get_customers_from_team(test_session, employee_with_team_factory, team_factory):
    team = team_factory.create()
    employee_with_team_factory.create_batch(4, assignment__team=team)
    other_employee = employee_with_team_factory.create(guest=True)
    result = get_employees_from_team(test_session, team_name=team.name)
    assert len(result) == 4
    assert other_employee.teams[0].name != team.name
