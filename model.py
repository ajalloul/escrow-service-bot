from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

from config import *

Base = declarative_base()

engine = create_engine(
    os.getenv("DATABASE_URL"),
    echo=True)
#    connect_args={'check_same_thread': False},




class Trade(Base):
    """
    SqlAlchemy ORM Trade Model
    """
    __tablename__ = 'trades'

    id = Column(String, primary_key=True)

    seller = Column(Integer)
    buyer = Column(Integer)
    price = Column(Integer)

    currency = Column(String)
    coin = Column(String)
    wallet = Column(String)

    payment_status = Column(Boolean)
    created_at = Column(String)
    updated_at = Column(String)
    is_open = Column(Boolean)

    receive_address_id = Column(String)

    dispute = relationship("Dispute", cascade="all")

    def __repr__(self):
        return "<Trade(id='%s')>" % (self.id)

    def is_dispute(self):
        "Dispute Status"
        if self.dispute == []:
            return "No Dispute"
        else:
            return "%s Created on %s " % (self.dispute[-1].id, self.dispute[-1].created_on)


class Dispute(Base):
    """
    SQLAlchemy ORM Dispute Model
    """
    __tablename__ = "disputes"

    id = Column(String, unique=True, primary_key=True)
    user = Column(Integer)
    complaint = Column(String)
    created_on = Column(String)
    trade_id = Column(ForeignKey("trades.id"))

    trade = relationship("Trade", uselist=False)

    def is_seller(self):
        if self.user == self.trade[0].seller:
            return True
        else:
            return False

    def is_buyer(self):
        if self.user == self.trade[0].buyer:
            return True
        else:
            return False


# Base.metadata.drop_all(bind=engine)
# Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine, autoflush=False)

session = Session()

import pdb; pdb.set_trace()
session.close()