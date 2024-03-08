from django.db import models

class District(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(to = 'State', on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return f"{self.name}, {self.state}"