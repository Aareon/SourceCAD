from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sqlite3

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(length=255), unique=True, nullable=True)
    username = Column(String(length=32), unique=True, nullable=True)
    pass_hash = Column(String(length=255), unique=True, nullable=False)
    unit_number = Column(String(length=4), unique=True, nullable=True, default='')
    rank = Column(String(length=54), unique=False, nullable=True, default='')
    is_civilian = Column(Integer, unique=False, default=0)
    is_dispatch = Column(Integer, unique=False, default=0)
    is_police = Column(Integer, unique=False, default=0)
    is_admin = Column(Integer, unique=False, default=0)

    def __repr__(self):
        return '<User(id={0}, email=\'{1}\', username=\'{2}\', pass_hash=\'{3}\', \
        is_civilian={4}, is_dispatch{5}, is_police={6})>'.format(self.id,
                                                                 self.email,
                                                                 self.username,
                                                                 self.pass_hash,
                                                                 self.is_civilian,
                                                                 self.is_dispatch,
                                                                 self.is_police)

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True, nullable=False)
    name = Column(String(length=255), nullable=True)
    age = Column(Integer, unique=False, nullable=False)
    address = Column(String(length=255), default='Homeless')
    drivers_license = Column(Boolean, default=True, nullable=False)
    ccp_license = Column(Boolean, default=False, nullable=False)
    ocp_license = Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return '<Character(id={0}, name=\'{1}\', age={2}, address=\'{3}\', \
        drivers_license={4}, ccp_license={5}, ocp_license={6})>'.format(self.id,
                                                                        self.age,
                                                                        self.address,
                                                                        self.drivers_license,
                                                                        self.ccp_license,
                                                                        self.ocp_license)

class Registration(Base):
    __tablename__ = 'registrations'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True, nullable=False)
    owner = Column(ForeignKey('characters.id'))
    make = Column(String(32), nullable=False)
    model = Column(String(32), nullable=False)
    tag_number = Column(String(16), nullable=False)
    insurance = Column(Boolean, default=True, nullable=False)

    def __repr__(self):
        return '<Registration(id={0}, owner=\'{1}\', make=\'{2}\', model=\'{3}\', \
        tag_number=\'{4}\', insurance={5})>'.format(self.id,
                                                    self.owner,
                                                    self.make,
                                                    self.model,
                                                    self.tag_number,
                                                    self.insurance)

class Bolo(Base):
    __tablename__ = 'bolos'

    id = Column(Integer, primary_key=True, nullable=False)
    reason = Column(String(length=140), nullable=True)
    location = Column(String(length=255), nullable=True)
    description = Column(String(length=255), nullable=True)
    notes = Column(String(length=255), nullable=True)

    def __repr__(self):
        return '<BOLO(id={0}, author=\'{1}\', reason=\'{2}\', last_seen=\'{3}\', \
        description=\'{4}\', notes=\'{5}\')>'.format(self.id,
                                                     self.author,
                                                     self.reason,
                                                     self.last_seen,
                                                     self.description,
                                                     self.notes)

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True, nullable=False)
    author = Column(ForeignKey('users.id'), nullable=False)
    offender = Column(ForeignKey('users.id'), nullable=False)
    penal_code = Column(String(length=16), nullable=False)
    punishment = Column(String(length=32), nullable=True) # nullable in case its something like a fix-it ticket
    notes = Column(String(length=140), nullable=True)

    def __repr__(self):
        return '<Ticket(id={0}, author=\'{1}\', offender=\'{2}\', \
        penal_code=\'{3}\', punishment=\'{4}\', notes=\'{5}\')>'.format(self.id,
                                                                        self.author,
                                                                        self.offender,
                                                                        self.penal_code,
                                                                        self.punishment,
                                                                        self.notes)

class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True, nullable=False)
    unit = Column(ForeignKey('users.id'), nullable=False)
    code = Column(String(length=255), nullable=False)

    def __repr__(self):
        return '<Activity(id={0}, unit=\'{1}\', code=\'{2}\')>'.format(self.id,
                                                                       self.unit,
                                                                       self.code)

class Callout(Base):
    __tablename__ = 'callouts'

    id = Column(Integer, primary_key=True, nullable=False)
    reason = Column(String(length=255), nullable=True)
    location = Column(String(length=255), nullable=True)
    details = Column(String(length=255), nullable=True)
    present_units = Column(String(length=255), nullable=True)

    def __repr__(self):
        return '<Callout(id={0}, code=\'{1}\', reason=\'{2}\', location=\'{3}\', \
        present_units=\'{4}\')>'.format(self.id,
                                        self.code,
                                        self.reason,
                                        self.location,
                                        self.present_units)

class Database:
    def __init__(self):
        self.engine = create_engine('sqlite:///sourcecad.db?check_same_thread=False', echo=False)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def get_password(self, item, use_email=False, use_unit_number=False):
        # if neither methods are specified
        if not use_email and not use_unit_number:
            return

        # protect against bots? trying to do more than one thing at once, kind of
        if use_email and use_unit_number:
            raise SyntaxError('Too many things to select. Choose email or unit_number, not both.')

        try:
            # get user data using email
            if use_email:
                id, pass_hash = self.session.query(User.id, User.pass_hash).filter_by(email=item).all()[0]

            # get user data using unit number
            if use_unit_number:
                id, pass_hash = self.session.query(User.id, User.pass_hash).filter_by(unit_number=item).all()[0]

            # return the id as well as the encoded password hash and salt ready for hashing and verifying
            return (id, pass_hash)
        except:
            # something happened. Oh well
            return (None, None)

    def get_user_info(self, id=None):
        # start integrating errors
        if id is None:
            return {'errors': 'Invalid session. Try logging back in'}

        try:
            return self.session.query(User.email,
                                      User.username,
                                      User.unit_number,
                                      User.rank,
                                      User.is_civilian,
                                      User.is_dispatch,
                                      User.is_police,
                                      User.is_admin).filter_by(id=id).all()[0]
        except:
            return (None, None, None, None, None, None, None, None, None)

    def get_callouts(self):
        return self.session.query(Callout.id, Callout.reason, Callout.location, Callout.details, Callout.present_units).all()

    def get_bolos(self):
        return self.session.query(Bolo.id, Bolo.reason, Bolo.location, Bolo.description, Bolo.notes).all()
