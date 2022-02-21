import factory
from factory.fuzzy import FuzzyChoice

from models import Employee, Customer, CustomerType, Team, TeamMembership
from crud import get_session

session = get_session()


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    id = factory.Faker('uuid4')

    class Meta:
        sqlalchemy_session = session
        # sqlalchemy_session_persistence = 'commit'


class EmployeeFactory(BaseFactory):
    class Meta:
        model = Employee


class TeamFactory(BaseFactory):
    class Meta:
        model = Team


class TeamMembershipFactory(BaseFactory):
    class Meta:
        model = TeamMembership
