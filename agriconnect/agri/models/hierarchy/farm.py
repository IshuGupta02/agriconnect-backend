# from django.db import models
# from village import Village

# class Farm(models.Model):
#     village = models.ForeignKey(Village, on_delete=models.CASCADE, related_name='farms')
#     coordinates = models.PointField()
#     area = models.FloatField()
#     farmer = models.ForeignKey(Farmer, on_delete=models.SET_NULL, null=True, blank=True, related_name='farms')

#     def __str__(self):
#         return f"Farm in {self.village} owned by {self.farmer if self.farmer else 'No Farmer'}"
