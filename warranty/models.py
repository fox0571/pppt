from django.db import models
from request.models import UnitBasicInfo
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,'Waiting'),
    (1,'Approved'),
    (2,'Disputed'),
    (3,'In-house'),
)

INVOICE_TYPE = (
	(0,'from service company'),
	(1,'from inhouse tech'),
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
	dispute_time = models.DateTimeField(null=True,blank=True)
	note = models.TextField(null=True,blank=True)
	file = models.FileField(null=True,blank=True,upload_to="invoice/")
	incident = models.ForeignKey(UnitBasicInfo, on_delete=models.CASCADE,null=True)
	status = models.IntegerField(choices=STATUS,default=0)
	invoice_type = models.IntegerField(choices=INVOICE_TYPE,default=0)
	dispute_note = models.TextField(null=True,blank=True)
	processed = models.BooleanField(default=False)
	voucher = models.CharField(max_length=15,default='------')
	approved_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
	approved_by = models.ForeignKey(User, related_name="approver",on_delete=models.CASCADE,null=True,blank=True)
	need_w9 = models.BooleanField(default=False)
	def __str__(self):
		return self.invoice+", "+self.sksid

	class Meta:
		ordering = ('add_time',)
		permissions = (
            ("approve_invoice", "Can approve or dispute invoice"),
			("process_invoice", "Can process invoice"),
        )

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
