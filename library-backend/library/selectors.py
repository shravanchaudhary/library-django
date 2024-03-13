from library.models import Books, Circulation, Members, Reservation
from datetime import timedelta
from django.utils import timezone

# TODO: Add member in queryselectors for all model for permission management
# TODO: proper error handling when object(s) not found


class BooksSelector:

    @classmethod
    def get_queryset(cls):
        return Books.objects.all()

    @classmethod
    def get_object(cls, **kwargs):
        qs = cls.get_queryset().filter(**kwargs)
        if not qs.exists():
            return None
        return qs.first()


class CirculationSelector:

    @classmethod
    def get_queryset(cls):
        return Circulation.objects.all().select_related("book", "member")

    @classmethod
    def get_object(cls, **kwargs):
        qs = cls.get_queryset().filter(**kwargs)
        if not qs.exists():
            return None
        return qs.first()


class ReservationSelector:

    @classmethod
    def get_queryset(cls):
        return Reservation.objects.all().select_related("book", "member")

    @classmethod
    def get_object(cls, **kwargs):
        qs = cls.get_queryset().filter(**kwargs)
        if not qs.exists():
            return None
        return qs.first()

    @classmethod
    def get_first_reservation(cls, book_id):
        qs = (
            cls.get_queryset()
            .filter(book_id=book_id, fulfilled=False)
            .order_by("timestamp")
        )
        if not qs.exists():
            return None
        return qs.first()


class MembersSelector:

    @classmethod
    def get_queryset(cls):
        return Members.objects.all()

    @classmethod
    def get_object(cls, **kwargs):
        qs = cls.get_queryset().filter(**kwargs)
        if not qs.exists():
            return None
        return qs.first()

    @classmethod
    def get_overdue_books(cls, member_id):
        checkout_days = 0
        overdue_books = CirculationSelector.get_queryset().filter(
            member_id=member_id,
            checkedout=True,
            returned=False,
            timestamp__lte=timezone.now() - timedelta(days=checkout_days),
        ).values_list("book_id", flat=True)
        return BooksSelector.get_queryset().filter(id__in=overdue_books)


