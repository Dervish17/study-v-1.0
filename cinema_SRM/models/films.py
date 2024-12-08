from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import Base


class Film(Base):
    __tablename__ = 'films'

    film_id = Column(Integer, primary_key=True, index=True)
    film_name = Column(String, nullable=False)
    film_author = Column(String, nullable=False)
    film_genre = Column(String,nullable=False)
    film_time = Column(String, nullable=False)
    film_release = Column(String, nullable=False)
    film_rating = Column(Float, nullable=False)

    screening = relationship('Screening', back_populates='film')
