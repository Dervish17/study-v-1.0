from PyQt6.QtWidgets import QApplication
from app.mainWin import MainWindow
import sys
import traceback

from database import init_db, SessionLocal
from services.film_service import FilmService


def main():
    init_db()
    db = SessionLocal()
    try:
        film_service = FilmService(db)
        film_service.add_film(film_name='Титаник', film_author='Джеймс Кэмерон', film_genre='Романтика', film_time='03:14', film_release='01.11.1997 12:00', film_rating=8.4)
        film_service.add_film(film_name='Человек-паук', film_author='Сэм Рэйми', film_genre='Фантастика', film_time='02:01', film_release='01.05.2002 12:00', film_rating=7.7)
        film_service.add_film(film_name='1+1', film_author='Оливье Накаш, Эрик Толерандо', film_genre='Драма', film_time='01:52', film_release='26.04.2012 12:00', film_rating=8.8)
        film_service.add_film(film_name='Интерстеллар', film_author='Кристофер Нолан', film_genre='Фантастика', film_time='02:49', film_release='06.11.2014 12:00', film_rating=8.6)
        film_service.add_film(film_name='Бойцовский клуб', film_author='Дэвид Финчер', film_genre='Драма', film_time='02:19', film_release='13.01.1999 12:00', film_rating=8.7)
        film_service.add_film(film_name='Джентльмены', film_author='Гай Ричи', film_genre='Боевик', film_time='01:53', film_release='13.02.2020 12:00', film_rating=8.6)
        film_service.add_film(film_name='Криминальное чтиво', film_author='Квентин Тарантино', film_genre='Драма', film_time='02:34', film_release='29.09.1994 12:00', film_rating=8.7)
        film_service.add_film(film_name='Назад в будущее', film_author='Роберт Земекис', film_genre='Фантастика', film_time='01:56', film_release='27.06.2013 12:00', film_rating=8.6)
        film_service.add_film(film_name='Гарри Поттер и философский камень', film_author='Крис Коламбус', film_genre='Фантастика', film_time='02:32', film_release='21.03.2002 12:00', film_rating=8.3)
        film_service.add_film(film_name='Крестный отец', film_author='Френсис Форд Коппола', film_genre='Драма', film_time='02:55', film_release='03.02.1992 12:00', film_rating=8.7)

    finally:
        db.close()
    app = QApplication([])
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))


sys.excepthook = excepthook

if __name__ == '__main__':
    main()
