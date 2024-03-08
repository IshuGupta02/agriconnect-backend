from django.db import models

class CropMSP(models.Model):
    crop = models.ForeignKey(to='Crop', on_delete=models.CASCADE)
    msp = models.FloatField()
    country = models.ForeignKey(to = 'Country', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.crop} - MSP: {self.msp}"

class Country(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name