from django.db import models
from .person import Person

class Farmer(Person):
    ID_CARD_CHOICES = [
        ('aadhar', 'Aadhar Card'),
        ('passport', 'Passport'),
        ('driving_license', 'Driving License'),
    ]

    id_card_type = models.CharField(max_length=20, choices=ID_CARD_CHOICES)
    id_card_number = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)
    is_bpl = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - Farmer"
