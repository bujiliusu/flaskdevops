import sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:123456@localhost/devops', echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
print(sqlalchemy.__version__)


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return '<Student {} {} {}>'.format(self.id, self.name, self.age)

print(repr(Student.__table__))
s = Student(name='tom')
s.age = 30
print(s)
print(Student.__table__)
# Base.metadata.create_all(engine)
session.add(s)
session.commit()