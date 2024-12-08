from sqlalchemy.orm import Session
from models.tickets import Ticket


class TicketService:
    def __init__(self, db: Session):
        self.db = db

    def add_ticket(self, screening_id: int, ticket_row: int, ticket_seat: int, ticket_status: str):
        new_ticket = Ticket(
            screening_id=screening_id,
            ticket_row=ticket_row,
            ticket_seat=ticket_seat,
            ticket_status=ticket_status
        )
        self.db.add(new_ticket)
        self.db.commit()
        self.db.refresh(new_ticket)
        return new_ticket

    def get_booked_seats(self, screening_id):
        seats = self.db.query(Ticket).filter_by(screening_id=screening_id, ticket_status='booked').all()
        return seats

    def delete_tickets(self, screening_id):
        with self.db.begin():
            tickets_to_delete = self.db.query(Ticket).get(screening_id)
            if tickets_to_delete:
                self.db.delete(tickets_to_delete)
                return True
            else:
                return False