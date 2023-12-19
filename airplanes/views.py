from rest_framework import generics, status
from rest_framework.response import Response

from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneListCreateView(generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def create(self, request, *args, **kwargs):
        airplanes_data = request.data

        if len(airplanes_data) > 10:
            return Response({"detail": "Cannot create more than 10 airplanes."}, status=status.HTTP_400_BAD_REQUEST)
        
        if not isinstance(airplanes_data, list):
            return Response({"detail": "Invalid data. Expected a list of dictionaries."}, status=status.HTTP_400_BAD_REQUEST)

        created_airplanes = []

        for airplane_data in airplanes_data:
            serializer = self.get_serializer(data=airplane_data)
            serializer.is_valid(raise_exception=True)

            instance = serializer.save()
            fuel_consumption = instance.fuel_consumption_per_minute()
            max_flight_minutes = instance.fuel_tank_capacity() / fuel_consumption

            response_data = {
                "id": instance.id,
                "passenger_assumptions": instance.passenger_assumptions,
                "fuel_consumption_per_minute": fuel_consumption,
                "max_flight_minutes": max_flight_minutes
            }

            created_airplanes.append(response_data)

        return Response(created_airplanes, status=status.HTTP_201_CREATED)

