from django.db import models
import math

class Airplane(models.Model):
    id = models.IntegerField(primary_key=True)
    passenger_assumptions = models.IntegerField()

    def fuel_tank_capacity(self):
        return 200 * self.id

    def fuel_consumption_per_minute(self):
        base_consumption = 0.80 * math.log10(self.id)
        additional_consumption = 0.002 * self.passenger_assumptions
        return base_consumption + additional_consumption
