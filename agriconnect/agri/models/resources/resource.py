from django.db import models

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('seed', 'Seed'),
        ('fertilizer', 'Fertilizer'),
        ('manure', 'Manure'),
        ('pesticide', 'Pesticide'),
    ]

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=RESOURCE_TYPES)

    def __str__(self):
        return self.name
