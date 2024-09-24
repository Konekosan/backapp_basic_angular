from app.app_config.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

user_roles = Table(
    'User_roles', Base.metadata,
    Column('user_id', Integer, ForeignKey('Usager.id')),
    Column('role_id', Integer, ForeignKey('Role.id'))
)

role_permissions = Table(
    'Role_permissions', Base.metadata,
    Column('role_id', Integer, ForeignKey('Role.id')),
    Column('permission_id', Integer, ForeignKey('Permission.id'))
)

class Usager(Base):
    __tablename__='Usager'

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, index=True)
    prenom = Column(String, index=True)
    age = Column(Integer, index=True)
    username = Column(String, unique=True)
    hashed_pwd = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    roles = relationship('Role', secondary=user_roles, back_populates='usagers')

class Role(Base):
    __tablename__='Role'

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True, index=True)
    usagers = relationship('Usager', secondary=user_roles, back_populates='roles')
    permissions = relationship('Permission', secondary=role_permissions, back_populates='roles')

class Permission(Base):
    __tablename__ = 'Permission'
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, unique=True, index=True)
    roles = relationship('Role', secondary=role_permissions, back_populates='permissions')