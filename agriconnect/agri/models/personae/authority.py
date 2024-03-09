from django.db import models
from .person import Person

class Authority(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    report_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    farms = models.ManyToManyField(to='Farmer', related_name='authorities', blank=True)

    def __str__(self):
        return f"Authority {self.id}"