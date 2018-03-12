import sqlite3

from sqlalchemy import (Boolean, Column, ForeignKey, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(length=255), unique=True, nullable=True)
    username = Column(String(length=32), unique=True, nullable=True)
    password = Column(String(length=255), unique=True, nullable=False)
    unit_number = Column(String(length=4), unique=True,
                         nullable=True, default='')
    rank = Column(String(length=54), unique=False, nullable=True, default='')
    is_civilian = Column(Integer, unique=False, default=0)
    is_dispatch = Column(Integer, unique=False, default=0)
    is_police = Column(Integer, unique=False, default=0)
    is_admin = Column(Integer, unique=False, default=0)

    def __repr__(self):
        return '<User(id={0}, email=\'{1}\', username=\'{2}\', password=\'{3}\', \
        is_civilian={4}, is_dispatch{5}, is_police={6})>'.format(self.id,
                                                                 self.email,
                                                                 self.username,
                                                                 self.password,
                                                                 self.is_civilian,
                                                                 self.is_dispatch,
                                                                 self.is_police)


class Application(Base):
    __tablename__ = 'applications'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(length=255), unique=True, nullable=True)
    username = Column(String(length=32), unique=True, nullable=True)
    password = Column(String(length=255), unique=True, nullable=False)
    unit_number = Column(String(length=4), unique=True,
                         nullable=True, default='')
    rank = Column(String(length=54), unique=False, nullable=True, default='')
    is_civilian = Column(Integer, unique=False, default=0)
    is_dispatch = Column(Integer, unique=False, default=0)
    is_police = Column(Integer, unique=False, default=0)
    is_admin = Column(Integer, unique=False, default=0)

    def __repr__(self):
        return '<Application(id={0}, email=\'{1}\', username=\'{2}\', password=\'{3}\', \
        is_civilian={4}, is_dispatch{5}, is_police={6})>'.format(self.id,
                                                                 self.email,
                                                                 self.username,
                                                                 self.password,
                                                                 self.is_civilian,
                                                                 self.is_dispatch,
                                                                 self.is_police)


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, ForeignKey('users.id'),
                primary_key=True, nullable=False)
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

    id = Column(Integer, ForeignKey('users.id'),
                primary_key=True, nullable=False)
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
    # nullable in case its something like a fix-it ticket
    punishment = Column(String(length=32), nullable=True)
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

class Login(Base):
    __tablename__ = 'logins'

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(length=32), nullable=False)
    rank = Column(ForeignKey('users.rank'), unique=False, nullable=True)
    role = Column(String(length=16), nullable=False)
    login_date = Column(String(length=255), nullable=False)
    login_time = Column(String(length=255), nullable=False)

    def __repr__(self):
        return '<Login(id={0}, username=\'{1}\', rank=\'{2}\',\
                login_date=\'{3}\', login_time=\'{4}\',)>'.format(self.id,
                                                                  self.username,
                                                                  self.rank,
                                                                  self.login_date,
                                                                  self.login_time)


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
        self.engine = create_engine(
            'sqlite:///sourcecad.db?check_same_thread=False', echo=False)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def get_password(self, item, use_email=False, use_unit_number=False):
        # if neither methods are specified
        if not use_email and not use_unit_number:
            return

        # protect against bots? trying to do more than one thing at once, kind of
        if use_email and use_unit_number:
            raise SyntaxError(
                'Too many things to select. Choose email or unit_number, not both.')

        try:
            # get user data using email
            if use_email:
                id, password = self.session.query(
                    User.id, User.password).filter_by(email=item).all()[0]

            # get user data using unit number
            if use_unit_number:
                id, password = self.session.query(
                    User.id, User.password).filter_by(unit_number=item).all()[0]

            # return the id as well as the encoded password hash and salt ready for hashing and verifying
            return (id, password)
        except Exception as exc:
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

    def check_user_exists(self, username, email, unit_number):
        if email is None:
            q = self.session.query(User.username, User.unit_number).filter_by(
                username=username, unit_number=unit_number).all()
        else:
            q = self.session.query(User.username, User.unit_number, User.email).filter_by(
                username=username, unit_number=unit_number, email=email).all()
        if len(q) == 0:
            return False
        else:
            return True

    def create_applicant(self, username, email, unit_number, password, is_dispatch, is_civilian, is_police):
        """
        id: Integer, primary key
        email: String, unique
        username: String, unique
        password: String
        unit_number: String, unique
        rank: String
        is_civilian: Integer
        is_dispatch: Integer
        is_police: Integer
        is_admin: Integer
        """
        if not self.check_user_exists(username, email, unit_number):
            self.session.add(Application(email=email,
                                         username=username,
                                         password=password,
                                         unit_number=unit_number,
                                         is_civilian=is_civilian,
                                         is_dispatch=is_dispatch,
                                         is_police=is_police))
            self.session.commit()
            return True
        else:
            return False

    def approve_applicant(self, **kwargs):
        email, username = kwargs.get("email"), kwargs.get("username")
        applicant = self.session.query(Application).filter_by(email=email, username=username).first()
        self.session.add(User(email=applicant.email,
                              username=applicant.username,
                              password=applicant.password,
                              unit_number=applicant.unit_number,
                              is_civilian=applicant.is_civilian,
                              is_dispatch=applicant.is_dispatch,
                              is_police=applicant.is_police))
        self.session.delete(applicant)
        self.session.commit()
    
    def reject_applicant(self, **kwargs):
        email, username = kwargs.get("email"), kwargs.get("username")
        applicant = self.session.query(Application).filter_by(email=email, username=username).delete()
        self.session.commit()

    def get_callouts(self):
        return self.session.query(Callout.id, Callout.reason, Callout.location, Callout.details, Callout.present_units).all()

    def get_bolos(self):
        return self.session.query(Bolo.id, Bolo.reason, Bolo.location, Bolo.description, Bolo.notes).all()

    def get_applicants(self):
        return self.session.query(Application.username, Application.email, Application.is_civilian, Application.is_dispatch, Application.is_police).all()

    def add_login(self, username, rank, role):
        now = datetime.now()
        date = now.strftime('%Y-%m-%d')
        time = now.strftime('%H:%M')
        try:
            self.session.add(Login(username=username,
                                   rank=rank,
                                   role=role,
                                   login_date=date,
                                   login_time=time))
            self.session.commit()
        except:
            pass

    def get_logins(self):
        return self.session.query(Login.username, Login.rank, Login.login_date, Login.login_time).limit(5).all()
