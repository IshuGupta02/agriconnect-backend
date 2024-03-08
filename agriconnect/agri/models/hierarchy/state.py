from django.db import models

class State(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(to='Country', on_delete=models.CASCADE, related_name='states')

    def __str__(self):
        return f"{self.name}, {self.country}"