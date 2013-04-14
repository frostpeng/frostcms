#coding=utf-8
import transaction

from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base



from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    password = Column(String(50),nullable=False)
    role = Column(Integer, default=0)
    regtime=Column(Integer)
    lastlogin=Column(Integer)
    logintimes=Column(Integer)

def initialize_sql(engine):
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)