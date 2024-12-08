from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Ticket(Base):
    __tablename__ = 'tickets'

    ticket_id = Column(Integer, primary_key=True, index=True)
    screening_id = Column(Integer, ForeignKey('screenings.screening_id'))
    ticket_row = Column(Integer, nullable=False)
    ticket_seat = Column(Integer, nullable=False)
    ticket_status = Column(String, nullable=False)

    screening = relationship('Screening', back_populates='ticket')
