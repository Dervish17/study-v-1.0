from sqlalchemy.orm import Session
from models.cinema_hall import CinemaHall


class CinemaHallService:
    def __init__(self, db: Session):
        self.db = db

    def add_cinema_hall(self, cinema_hall_name: str, cinema_hall_capacity: int):
        new_cinema_hall = CinemaHall(
            cinema_hall_name=cinema_hall_name,
            cinema_hall_capacity=cinema_hall_capacity,
        )
        self.db.add(new_cinema_hall)
        self.db.commit()
        self.db.refresh(new_cinema_hall)
        return new_cinema_hall
