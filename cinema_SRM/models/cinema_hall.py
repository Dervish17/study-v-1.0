from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship


class CinemaHall(Base):
    __tablename__ = 'cinema_halls'

    cinema_hall_id = Column(Integer, primary_key=True, index=True)
    cinema_hall_name = Column(String, nullable=False)
    cinema_hall_capacity = Column(Integer, nullable=False)

    screening = relationship('Screening', back_populates='cinema_hall')
