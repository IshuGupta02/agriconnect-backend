from django.db import models
class FarmClaimRequest(models.Model):
    farm = models.ForeignKey(to='Farm', on_delete=models.CASCADE)
    farmer = models.ForeignKey(to='Farmer', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.farm} - {self.farmer}"