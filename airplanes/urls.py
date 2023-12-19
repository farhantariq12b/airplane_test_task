from django.urls import path
from .views import AirplaneListCreateView

urlpatterns = [
    path('airplanes/', AirplaneListCreateView.as_view(), name='airplane-list-create'),
]
