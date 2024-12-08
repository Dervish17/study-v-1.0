import traceback
from datetime import datetime
from sqlalchemy.orm import Session
from models.films import Film
from models.screening import Screening


class FilmService:
    def __init__(self, db: Session):
        self.db = db

    def add_film(self, film_name: str, film_author: str, film_genre: str, film_time: str,
                 film_release: str, film_rating: float):
        new_film = Film(
            film_name=film_name,
            film_author=film_author,
            film_genre=film_genre,
            film_time=film_time,
            film_release=film_release,
            film_rating=film_rating
        )

        print(
            f"Попытка добавить фильм: {film_name}, {film_author}, {film_genre}, "
            f"{film_time}, {film_release}, {film_rating}")

        try:
            self.db.add(new_film)
            self.db.commit()
            self.db.refresh(new_film)
            print("Фильм добавлен успешно")
        except Exception as e:
            self.db.rollback()
            print(f"Error occurred: {e}")
            print(traceback.format_exc())
            return None

        return new_film

    def all_films(self):
        # films = self.db.query(Film).join().all()
        films = self.db.query(Film).all()
        return films

    def get_names_films(self):
        names = self.db.query(Film.film_name).all()
        return names



    def convert_time_to_minutes(self, time_str):
        time_obj = datetime.strptime(time_str, "%H:%M:%S")
        return time_obj.hour * 60 + time_obj.minute

    def convert_release_date(self, release_str):
        return datetime.strptime(release_str, "%d-%m-%Y %H:%M")
