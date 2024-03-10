from django.db import models
from .person import Person

class Authority(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    report_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    farms = models.ManyToManyField(to='Farmer', related_name='authorities', blank=True)
    referral_code = models.CharField(max_length=20, null=True, blank=True, unique=True)

    def __str__(self):
        return f"Authority {self.id}"
