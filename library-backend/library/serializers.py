from rest_framework import serializers
from library.models import Books, Circulation, Reservation, Members


class BooksOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"


class ReservationOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class CirculationOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Circulation
        fields = "__all__"


class CirculationInputSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    member_id = serializers.IntegerField()
    checkedout = serializers.BooleanField(required=False)
    returned = serializers.BooleanField(required=False)


class ReservationInputSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()
    member_id = serializers.IntegerField()

class FulfillReservationInputSerializer(serializers.Serializer):
    book_id = serializers.IntegerField()

class FulfillReservationOutputSerializer(serializers.Serializer):
    reservation = ReservationOutputSerializer()
    circulation = CirculationOutputSerializer()


class MembersInputSerializer(serializers.Serializer):
    member_id = serializers.IntegerField()


class OverdueSerializer(serializers.Serializer):
    overdue = serializers.IntegerField()
    member_id = serializers.IntegerField()
