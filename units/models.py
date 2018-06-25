from django.db import models

# Create your models here.
class Part(models.Model):
    number=models.CharField(max_length=30)
    description_eng=models.CharField(max_length=90)
    description_chn=models.CharField(max_length=100)
    inventory=models.IntegerField(default=0)
    price_fob = models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    price_list = models.DecimalField(max_digits=7,decimal_places=2)
    price_enduser = models.DecimalField(max_digits=7,decimal_places=2)
    price_dealer = models.DecimalField(max_digits=7,decimal_places=2)
    price_partstown = models.DecimalField(max_digits=7,decimal_places=2)
    price_1 = models.DecimalField(max_digits=7,decimal_places=2,default=0.00)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ('number',)

class Unit(models.Model):
    model=models.CharField(max_length=30)
    description_eng=models.CharField(max_length=90)
    description_chn=models.CharField(max_length=100)
    parts=models.ManyToManyField(Part)
    def __str__(self):
        return self.model

    class Meta:
        ordering = ('model',)
