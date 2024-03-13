from library.models import Books, Circulation, Reservation
from library.selectors import (
    BooksSelector,
    CirculationSelector,
    MembersSelector,
    ReservationSelector,
)
from rest_framework.serializers import ValidationError
from django.db.transaction import atomic

# TODO: Write wrapper for integrity error
# TODO: Play on id of circulation instead of book_id and member_id

class CirculationServices:

    @classmethod
    @atomic
    def create_circulation(cls, data):
        book_id = data.get("book_id")
        member_id = data.get("member_id")
        book = BooksSelector.get_object(id=book_id)

        # Validations

        if data.get("checkedout"):
            if book.copies <= 0:
                raise ValidationError(
                    {"error": "No copies available, Please reserve the book"}
                )

            existing_checkout = CirculationSelector.get_object(
                book_id=book_id, member_id=member_id, checkedout=True, returned=False
            )
            if existing_checkout:
                raise ValidationError(
                    {"error": "Checkout exists, Please return the book first"}
                )

        if data.get("returned"):
            existing_checkout = CirculationSelector.get_object(
                book_id=book_id, member_id=member_id, checkedout=True, returned=False
            )
            if not existing_checkout:
                raise ValidationError(
                    {"error": "No checkout exists, Please checkout the book first"}
                )

        # Operations
        if data.get("checkedout"):
            book.copies -= 1
            book.save()
            circulation = Circulation.objects.create(**data)
        elif data.get("returned"):
            book.copies += 1
            book.save()
            circulation = existing_checkout
            circulation.returned = True
            circulation.save()
            # try:
            #     ReservationServices.fulfill_reservation({"book_id": book.id})
            # except ValidationError as e:
            #     pass
        else:
            raise ValidationError({"error": "Invalid operation"})
        
        return circulation


class ReservationServices:

    @classmethod
    @atomic
    def create_reservation(cls, data):
        book_id = data.get("book_id")
        book = BooksSelector.get_object(id=book_id)
        if book.copies > 0:
            raise ValidationError(
                {"error": "Copies available, Please checkout the book"}
            )
        return Reservation.objects.create(**data)

    @classmethod
    @atomic
    def fulfill_reservation(cls, data):
        book_id = data.get("book_id")
        reservation = ReservationSelector.get_first_reservation(book_id)
        if not reservation:
            raise ValidationError({"error": "No reservation exists"})
        reservation.fulfilled = True
        reservation.save()
        circulation = CirculationServices.create_circulation(
            {
                "book_id": book_id,
                "member_id": reservation.member_id,
                "checkedout": True
            }
        )
        return {"reservation": reservation, "circulation": circulation}


class MembersServices:

    @classmethod
    def get_overdue(cls, data):
        fine = 50
        overdue = 0
        overdue_books = MembersSelector.get_overdue_books(data.get("member_id"))
        if overdue_books:
            overdue = fine * overdue_books.count()
        return {"member_id": data.get("member_id"), "overdue": overdue}
