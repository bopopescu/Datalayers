from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#==========================================================================================#

from sqlalchemy import Column,  String,Integer,Sequence

class User(Base):
    __tablename__ = 'user'
    user = Column(String, primary_key=True)
    host = Column(String, primary_key=True)

    def __repr__(self):
        return "<User(name='%s')>" % (self.user)

#==========================================================================================#

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  Column,  String, MetaData

metadata = MetaData()


some_engine = create_engine('mysql+pymysql://root:root@localhost/mysql')

# create a configured "Session" class
Session = sessionmaker(bind=some_engine)

# create a Session
session = Session()

# work with sess
#root_user = User(user='root')
print(session.query(User).filter_by(user='root').first().host)

session.close_all()
session.commit()
print (session.query(User).filter_by(user='root').first())

#==========================================================================================#