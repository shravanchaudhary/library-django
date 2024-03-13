from django.urls import path
from library.views import *

# TODO: use routers for including viewsets
app_name = "library"

urlpatterns = [
    path('circulate', create_circulation, name="create_circulation"),
    path('reserve', create_reservation, name="create_reservation"),
    path('fulfill', fulfill_reservation, name="fulfill_reservation"),
    path('overdue', get_overdue, name="get_overdue"),
]