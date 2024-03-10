from django.db import models
from .person import Person

class Farmer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    is_bpl = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.person.name} - Farmer"
