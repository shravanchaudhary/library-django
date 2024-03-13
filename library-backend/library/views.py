from rest_framework.response import Response
from library.serializers import *
from library.services import *
from rest_framework.decorators import api_view
# TODO: Create proper viewsets

@api_view(["GET"])
def health_check(request):
    return Response({"ping": "pong"}, status=200)

@api_view(["POST"])
def create_circulation(request):
    input_serializer = CirculationInputSerializer
    output_serializer = CirculationOutputSerializer
    serializer = input_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    result = CirculationServices.create_circulation(data)
    output_serializer = output_serializer(result)
    return Response(output_serializer.data, status=201)

@api_view(["POST"])
def create_reservation(request):
    input_serializer = ReservationInputSerializer
    output_serializer = ReservationOutputSerializer
    serializer = input_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    result = ReservationServices.create_reservation(data)
    output_serializer = output_serializer(result)
    return Response(output_serializer.data, status=201)

@api_view(["POST"])
def fulfill_reservation(request):
    input_serializer = FulfillReservationInputSerializer
    output_serializer = FulfillReservationOutputSerializer
    serializer = input_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    result = ReservationServices.fulfill_reservation(data)
    output_serializer = output_serializer(result)
    return Response(output_serializer.data, status=201)

@api_view(["POST"])
def get_overdue(request):
    input_serializer = MembersInputSerializer
    output_serializer = OverdueSerializer
    serializer = input_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data
    result = MembersServices.get_overdue(data)
    output_serializer = output_serializer(result)
    return Response(output_serializer.data, status=200)