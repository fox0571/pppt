from django.db import models
from request.models import UnitBasicInfo
# Create your models here.
class Invoice(models.Model):
	invoice = models.CharField(max_length=20,null=True)
	travel_t = models.DecimalField(max_digits=5, decimal_places=2,null=True)
	labor_t = models.DecimalField(max_digits=5, decimal_places=2,null=True)
	travel_c = models.DecimalField(max_digits=7, decimal_places=2,null=True)
	labor_c = models.DecimalField(max_digits=7, decimal_places=2,null=True)
	material_c = models.DecimalField(max_digits=7, decimal_places=2,null=True)
	total_c = models.DecimalField(max_digits=7, decimal_places=2,null=True)
	sksid = models.CharField(max_length=30,null=True,blank=True)
	add_time = models.DateTimeField(auto_now_add=True,blank=True)
	note = models.TextField(null=True,blank=True)
	file = models.FileField(null=True,blank=True,upload_to="invoice/")
	incident = models.ForeignKey(UnitBasicInfo, on_delete=models.CASCADE,null=True)
	def __str__(self):
		return self.invoice+", "+self.sksid
