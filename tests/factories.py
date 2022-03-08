import factory
from factory.fuzzy import FuzzyChoice, FuzzyDate
from datetime import date, datetime

from models import Employee, Team, TeamMembership, CustomerType, Customer
from crud import get_session

session = get_session()


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Faker('uuid4')

    class Meta:
        sqlalchemy_session = session
        sqlalchemy_session_persistence = 'flush'


class EmployeeFactory(BaseFactory):
    class Meta:
        model = Employee
        sqlalchemy_get_or_create = ('sesa',)

    sesa = factory.Sequence(lambda x: f'SESA1{x}')
    name = factory.Faker('name', locale='pl_PL')
    date_of_birth = FuzzyDate(start_date=date(1990, 1, 1), end_date=date(2000, 12, 12))
    agreement_start = factory.LazyFunction(datetime.now)

    class Params:
        guest = factory.Trait(
            sesa=factory.Sequence(lambda x: f'GUEST1{x}'),
            name=factory.Faker('name', locale='en_GB')
        )


class TeamFactory(BaseFactory):
    class Meta:
        model = Team

    name = factory.Faker('job')


class TeamMembershipFactory(BaseFactory):
    class Meta:
        model = TeamMembership

    class Params:
        employee = factory.SubFactory(EmployeeFactory)
        team = factory.SubFactory(TeamFactory)

    employee_id = factory.LazyAttribute(lambda x: x.employee.id)
    team_id = factory.LazyAttribute(lambda x: x.team.id)


class EmployeeWithTeamFactory(EmployeeFactory):
    assignment = factory.RelatedFactory(TeamMembershipFactory, factory_related_name='employee')


class CustomerTypeFactory(BaseFactory):
    class Meta:
        model = CustomerType

    name = factory.Sequence(lambda x: f'Type {x + 1}')
    zone = factory.Faker('locale')
    priority = FuzzyChoice([1, 2, 3])


class CustomerFactory(BaseFactory):
    class Meta:
        model = Customer

    name = factory.Faker('company')
    address = factory.Faker('address')
    employee = factory.SubFactory(EmployeeFactory)
    employee_id = factory.LazyAttribute(lambda x: x.employee.id)
    last_purchase_date = factory.LazyFunction(datetime.now)
    customer_type = factory.SubFactory(CustomerTypeFactory)
    customer_type_id = factory.LazyAttribute(lambda x: x.customer_type.id)
