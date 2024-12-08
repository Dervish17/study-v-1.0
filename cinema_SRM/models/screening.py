from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Screening(Base):
    __tablename__ = 'screenings'

    screening_id = Column(Integer, primary_key=True, index=True)
    film_id = Column(Integer, ForeignKey('films.film_id'))
    cinema_hall_id = Column(Integer, ForeignKey('cinema_halls.cinema_hall_id'))
    screening_begin = Column(String, nullable=False)
    screening_date = Column(String, nullable=False)

    film = relationship('Film', back_populates='screening')
    cinema_hall = relationship('CinemaHall', back_populates='screening')
    ticket = relationship('Ticket', back_populates='screening')
