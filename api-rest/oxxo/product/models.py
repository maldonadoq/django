from django.db import models

# Create your models here.

class Beer(models.Model):
    mark = models.CharField(max_length=40)
    alcohol = models.DecimalField(max_digits=4, decimal_places=2)
    ml = models.IntegerField()
    handmade = models.BooleanField()
    nationality = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.mark
