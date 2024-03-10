from django.contrib.auth.models import AbstractUser
from django.db import models

class Person(AbstractUser):
    ID_CARD_CHOICES = [
        ('aadhar', 'Aadhar Card'),
        ('passport', 'Passport'),
        ('driving_license', 'Driving License'),
    ]
    mobile = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=255)

    id_card_type = models.CharField(max_length=20, choices=ID_CARD_CHOICES)
    id_card_number = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username
