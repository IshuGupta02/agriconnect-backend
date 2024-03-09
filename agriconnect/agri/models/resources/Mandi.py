from django.db import models

class Mandi(models.Model):
    # coordinates = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Mandi: {self.coordinates}"
    
class CropPrice(models.Model):
    mandi = models.ForeignKey(Mandi, on_delete=models.CASCADE)
    crop = models.ForeignKey(to ='Crop', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.crop_name} - {self.price}"