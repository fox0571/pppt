from django.db import models
from request.models import UnitBasicInfo
# Create your models here.

STATUS = (
    (0,'Waiting'),
    (1,'Approved'),
    (2,'Disputed'),
    (3,'In-house'),
)
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
	status = models.IntegerField(choices=STATUS,default=0)
	dispute_note = models.TextField(null=True,blank=True)
	processed = models.BooleanField(default=False)
	voucher = models.CharField(max_length=15,default='------')
	approved_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	need_w9 = models.BooleanField(default=False)
	def __str__(self):
		return self.invoice+", "+self.sksid

	class Meta:
		ordering = ('add_time',)

class Sales(models.Model):
	sn = models.CharField(max_length=50)
	item_id = models.CharField(max_length=20)
	branch_id = models.CharField(max_length=5)
	customer_id = models.IntegerField()
	bill2_name = models.CharField(max_length=100)
	transaction = models.IntegerField()
	date = models.DateTimeField()
	ship2_contact = models.CharField(max_length=50, null=True, blank=True)
	ship2_name = models.CharField(max_length=50)
	ship2_address1 = models.CharField(max_length=50)
	ship2_address2 = models.CharField(max_length=50, null=True, blank=True)
	ship2_city = models.CharField(max_length=50)
	ship2_state = models.CharField(max_length=50)
	ship2_zip = models.CharField(max_length=50)

	def __str__(self):
		return self.sn
