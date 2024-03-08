from django.db import models

class Village(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey( to= 'District', on_delete=models.CASCADE, related_name='villages')

    def __str__(self):
        return f"{self.name}, {self.district}"