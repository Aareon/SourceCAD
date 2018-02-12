from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import bcrypt
import psycopg2

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(length=255), unique=True, nullable=True)
    username = Column(String(length=32), unique=True, nullable=True)
    pass_hash = Column(String(length=255), unique=True, nullable=False)
    pass_salt = Column(String(length=255), unique=True, nullable=False)
    is_civilian = Column(Boolean, unique=False, default=False)
    is_dispatch = Column(Boolean, unique=False, default=False)
    is_police = Column(Boolean, unique=False, default=False)


    def __repr__(self):
        return '<User(id={0}, email='{1}', username='{2}', pass_hash='{3}', \
        is_civilian={4}, is_dispatch{5}, is_police={6})>'.format(self.id,
                                                                 self.email,
                                                                 self.username
                                                                 self.pass_hash,
                                                                 self.is_civilian,
                                                                 self.is_dispatch,
                                                                 self.is_police)

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(length=255), primary_key=True, nullable=True)
    age = Column(Integer, unique=False, nullable=False)
    address = Column(String(length=255), default='Homeless')
    drivers_license = Column(Boolean, default=True, nullable=False)
    ccp_license = Column(Boolean, default=False, nullable=False)
    ocp_license = Column(Boolean, default=False, nullable=False)

class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, ForeignKey('users.id'))
    owner = Column(ForeignKey('characters.id'))
    make = Column(String(32), nullable=False)
    model = Column(String(32), nullable=False)
    tag_number = Column(String(16), nullable=False)
    insurance = Column(Boolean, default=True, nullable=False)

class Database:
    def __init__(self):
        self.engine = create_engine('sqlite+sqlite3:///sourcecad.db?check_same_thread=False', echo=False)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)
