from django.contrib.gis.db import models
from django.db.models import Q
from agri.models.resources.resource import Resource
from agri.models.personae.authority import Authority
from agri.models.personae.farmer import Farmer

class Allotment(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    quantity = models.FloatField()
    distribution_location = models.PointField()
    last_date = models.DateField()
    giving_authority = models.ForeignKey(Authority, on_delete=models.CASCADE, related_name='given_allotments')
    
    # Using Q objects to allow either Authority or Farmer as the receiver
    receiver = models.ForeignKey(
        models.Q(Authority) | models.Q(Farmer),
        on_delete=models.CASCADE,
        related_name='received_allotments'
    )

    def __str__(self):
        return f"Allotment of {self.resource} - {self.quantity} to {self.receiver} by {self.giving_authority}"