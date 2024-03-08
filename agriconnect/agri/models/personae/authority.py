from django.db import models

class Authority(models.Model):
    report_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates')
    farms = models.ManyToManyField(to='Farmer', related_name='authorities')

    def __str__(self):
        return f"Authority {self.id}"