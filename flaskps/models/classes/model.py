# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String, Table, Time, text, Date, Integer, BigInteger
from sqlalchemy.orm import relationship
from flaskps.models.alchemy import Base

metadata = Base.metadata


class AppConfig(Base):
    __tablename__ = 'app_config'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False, unique=True)
    value = Column(String(255), nullable=False)


class Center(Base):
    __tablename__ = 'center'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False, unique=True)
    address = Column(String(45))
    city = Column(String(45))
    phone_number = Column(String(45))
    lat = Column(String(45))
    lng = Column(String(45))


class Permission(Base):
    __tablename__ = 'permission'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False, unique=True)
    public_name = Column(String(45))

    role = relationship('Role', secondary='role_permission')


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False, unique=True)

    user = relationship('User', secondary='user_role')


class Role_Permission(Base):
    __tablename__ = 'role_permission'
    
    id_role = Column(ForeignKey('role.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    id_permission = Column(ForeignKey('permission.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(45), nullable=False, unique=True)
    username = Column(String(45))
    password = Column(String(100))
    first_name = Column(String(45))
    last_name = Column(String(45))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime)
    bloqued = Column(String(45), nullable=False, server_default=text("'no'"))
    confirmed = Column(String(45), nullable=False, server_default=text("'no'"))
    id_city = Column(Integer)
    phone_number = Column(BigInteger)
    address = Column(String(45))
    birthday = Column(Date)
    document_number = Column(String(45))
    id_document_type = Column(Integer)
    photo = Column(String(45), nullable=False)



class User_role(Base):
    __tablename__ = 'user_role'
    
    id_user = Column(ForeignKey('user.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    id_role = Column(ForeignKey('role.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)


