import sqlalchemy
from sqlalchemy.orm import Session
from models.screening import Screening
from datetime import datetime
from models.films import Film
from models.cinema_hall import CinemaHall


class ScreeningService:
    def __init__(self, db: Session):
        self.db = db

    def add_screening(self, film_id: int, cinema_hall_id: int, screening_begin: str, screening_date: str):
        new_screening = Screening(
            film_id=film_id,
            cinema_hall_id=cinema_hall_id,
            screening_begin=screening_begin,
            screening_date=screening_date
        )
        self.db.add(new_screening)
        self.db.commit()
        self.db.refresh(new_screening)
        return new_screening

    def all_screenings(self):
        # try:
        screenings = self.db.query(Screening.screening_id,
                                   Film.film_name,
                                   Screening.screening_begin,
                                   Screening.screening_date,
                                   CinemaHall.cinema_hall_name).join(Film).join(CinemaHall).all()
        return screenings

    def delete_screening(self, screening_id):
        with self.db.begin():
            screening_to_delete = self.db.query(Screening).get(screening_id)
            if screening_to_delete:
                self.db.delete(screening_to_delete)
                return True
            else:
                return False

    def update_screening(self, screening_id: int, film_id: int,
                         cinema_hall_id: int, screening_begin: str, screening_date: str):
        screening = self.db.query(Screening).filter(Screening.screening_id == screening_id).first()
        try:
            if screening:
                screening.film_id = film_id
                screening.cinema_hall_id = cinema_hall_id
                screening.screening_begin = screening_begin
                screening.screening_date = screening_date
                self.db.commit()
        except Exception as e:
            self.db.rollback()
            print(e)


    def convert_time_to_minutes(self, time_str):
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        return time_obj.hour * 60 + time_obj.minute

    def convert_release_date(self, release_str):
        return datetime.strptime(release_str, "%d-%m-%Y %H:%M")

