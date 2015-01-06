from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()




from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Numeric, Table, ForeignKey
from sqlalchemy.orm import relationship

user_to_bid_table = Table('user_to_bid', Base.metadata,
                         Column('users.id', Integer, ForeignKey('users.id')),
                         Column('bids.id', Integer, ForeignKey('bids.id'))
                         )
item_to_bid_table = Table('item_to_bid', Base.metadata,
                          Column('items.id', Integer, ForeignKey('items.id')),
                          Column('bids.id', Integer, ForeignKey('bids.id'))
                          )

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    bidsss = relationship("Bid", secondary="item_to_bid", backref="thing")
    
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable = False)
    
    items = relationship("Item", backref="person")
    bidss = relationship("Bid", secondary="user_to_bid", backref="people")
    
    
    
class Bid(Base):
    __tablename__ = "bids"
    
    id = Column(Integer, primary_key=True)
    price_point = Column(Numeric, nullable=False)
    
    
Base.metadata.create_all(engine)