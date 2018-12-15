from django.db import models

BRANCHES=(
    ('Brea', 'HQ, Brea, CA'),
    ('Hayward', 'Hayward, CA'),
    ('Dallas', 'Dallas, TX'),
    ('Houston', 'Houston, TX'),
    ('Washington', 'Kent, WA'),
    ('Colorado', 'Aurora, CO'),
    ('Florida', 'Tampa, FL'),
    ('Illinois', 'Homer Glen, IL'),
    ('Georgia', 'Doraville, GA'),
    ('New Jersey', 'Fairfield, NJ'),
    ('Massachusetts', 'Westborough, MA'),
    ('Ohio', 'Groveport, OH'),
)
class Part(models.Model):
    number=models.CharField(max_length=30)
    name_eng=models.CharField(max_length=90)
    name_chn=models.CharField(max_length=100)
    description=models.CharField(max_length=100,default="part")
    inventory=models.IntegerField(default=0)
    price_fob = models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    price_list = models.DecimalField(max_digits=7,decimal_places=2)
    price_enduser = models.DecimalField(max_digits=7,decimal_places=2)
    price_dealer = models.DecimalField(max_digits=7,decimal_places=2)
    price_partstown = models.DecimalField(max_digits=7,decimal_places=2)
    price_1 = models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    after_market_code=models.CharField(max_length=50,null=True,blank=True)
    weight=models.IntegerField(default=0)

    def __str__(self):
        return self.number+self.name_eng

    class Meta:
        ordering = ('number',)

class Unit(models.Model):
    model=models.CharField(max_length=30)
    name_eng=models.CharField(max_length=90,null=True)
    name_chn=models.CharField(max_length=100,null=True,blank=True)
    dimension = models.CharField(max_length=100,null=True,blank=True)
    spec = models.CharField(max_length=100,null=True,blank=True)
    parts=models.ManyToManyField(Part,null=True,blank=True)
    def __str__(self):
        return self.model

    class Meta:
        ordering = ('model',)

class PO2China(models.Model):
    parts = models.OneToOneField(Part,on_delete=models.CASCADE,null=True,blank=True)

    # 0 - created
    # 1 - ordered
    # 2 - shipped
    # 3 - received
    status = models.IntegerField(default=0)
    qty = models.IntegerField(default=10)
    branch = models.CharField(max_length=50,choices=BRANCHES)
    created_time = models.DateTimeField(auto_now_add=True)
    ordered_time = models.DateTimeField(null=True,blank=True)
    shipped_time = models.DateTimeField(null=True,blank=True)
    received_time = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.branch
