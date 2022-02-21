import re
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import func, Column, DateTime, String, ForeignKey, Integer, Date
from sqlalchemy.orm import declared_attr, relationship, as_declarative


def camel_snake(text: str) -> str:
    return re.sub(r'([a-z])([A-Z])', r'\g<1>_\g<2>', text).lower()


def generate_uuid() -> str:
    return uuid.uuid4().hex


@as_declarative()
class Base:
    id = Column(UUID, primary_key=True, default=generate_uuid)
    created = Column(DateTime(timezone=True), server_default=func.now())
    modified = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    @declared_attr
    def __tablename__(cls):
        return camel_snake(cls.__name__)


class Employee(Base):
    sesa = Column(String(128), nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    teams = relationship('Team', secondary='team_membership', backref='employees')
    date_of_birth = Column(Date)
    agreement_start = Column(DateTime)


class Customer(Base):
    name = Column(String(128), nullable=False)
    employee = relationship('Employee', backref='customers')
    address = Column(String(128))
    employee_id = Column(UUID, ForeignKey('employee.id'), nullable=False)
    customer_type = relationship('CustomerType', backref='customers')
    customer_type_id = Column(UUID, ForeignKey('customer_type.id'))
    last_purchase_date = Column(DateTime)


class CustomerType(Base):
    name = Column(String(128), nullable=False)
    zone = Column(String(16))
    priority = Column(Integer)


class Team(Base):
    name = Column(String(128), nullable=False, unique=True)


class TeamMembership(Base):
    employee_id = Column(UUID, ForeignKey('employee.id'), nullable=False)
    team_id = Column(UUID, ForeignKey('team.id'), nullable=False)
