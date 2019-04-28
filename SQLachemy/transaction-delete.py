from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#==========================================================================================#

from sqlalchemy import Column,  String,Integer,Sequence

class django_migrations(Base):
    __tablename__ = 'django_migrations'
    id = Column(Integer, primary_key=True)
    app = Column(String)
    name = Column(String)
    applied = Column(String)

    def __repr__(self):
        return "<User(id='%s') , User(app='%s') , User(name='%s') , User(applied='%s')>" % (self.id,self.app,self.name,self.applied)

#==========================================================================================#


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  Column,  String, MetaData

metadata = MetaData()
Session = sessionmaker()

some_engine = create_engine('mysql://root:@localhost/test')
connection  = some_engine.connect()

# create a configured "Session" class
session = Session(bind=connection)
# def run_query():
#     print(session.query(User).filter_by(user='root').first().host)
test1 = session.query(django_migrations).filter_by(id='1').first()
print (test1.id)
ins  = inspect(test1)
print('Transient: {0}; Pending: {1}; Persistent: {2}; Detached: {3}'.format(ins.transient, ins.pending, ins.persistent, ins.detached))
session.delete(test1)
print('Transient: {0}; Pending: {1}; Persistent: {2}; Detached: {3}'.format(ins.transient, ins.pending, ins.persistent, ins.detached))
# work with sess
print('Transient: {0}; Pending: {1}; Persistent: {2}; Detached: {3}'.format(ins.transient, ins.pending, ins.persistent, ins.detached))
session.commit()
print('Transient: {0}; Pending: {1}; Persistent: {2}; Detached: {3}'.format(ins.transient, ins.pending, ins.persistent, ins.detached))
session.close()
print('Transient: {0}; Pending: {1}; Persistent: {2}; Detached: {3}'.format(ins.transient, ins.pending, ins.persistent, ins.detached))
#==========================================================================================#
