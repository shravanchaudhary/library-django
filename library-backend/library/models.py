from django.db import models
from django.db.models import Q


class Books(models.Model):
    """Model for books."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    copies = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_book')
        ]

class Members(models.Model):
    """Model for members."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_member')
        ]

class Circulation(models.Model):
    """Model to track the circulation of books.
    Fields:
        1. book
        2. member
        3. timestamp
    """
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    checkedout = models.BooleanField(default=True)
    returned = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["book", "member"],
                condition=Q(returned=False, checkedout=True),
                name="unique_circulation",
            ),
        ]
    
class Reservation(models.Model):
    """Model to track the reservations of books.
    Fields:
        1. book
        2. member
        3. timestamp
    """
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['book', 'member'], condition=Q(fulfilled=False), name='unique_reservation')
        ]
