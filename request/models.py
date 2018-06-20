from django.db import models
from django.forms import ModelForm

SHIPPING_METHOD = (
    ('NDA','NEXT DAY AIR'),
    ('2NDA','SECOND DAY AIR'),
    ('GROUND','GROUND'),
)
STATES = (
    ("AL","Alabama"),("AK","Alaska"),("AS","American Samoa"),("AZ","Arizona"),
    ("AR","Arkansas"),("CA","California"),("CO","Colorado"),("CT","Connecticut"),
    ("DE","Delaware"),("DC","District Of Columbia"),("FM", "Federated States Of Micronesia"),
    ("FL", "Florida"),("GA", "Georgia"),("GU", "Guam"),("HI", "Hawaii"),("ID", "Idaho"),
    ("IL", "Illinois"),("IN", "Indiana"),("IA", "Iowa"),("KS", "Kansas"),("KY", "Kentucky"),
    ("LA", "Louisiana"),("ME", "Maine"),("MH", "Marshall Islands"),("MD", "Maryland"),
    ("MA", "Massachusetts"),("MI", "Michigan"),("MN", "Minnesota"),("MS", "Mississippi"),
    ("MO", "Missouri"),("MT", "Montana"),("NE", "Nebraska"),("NV", "Nevada"),
    ("NH", "New Hampshire"),("NJ", "New Jersey"),("NM", "New Mexico"),("NY", "New York"),
    ("NC", "North Carolina"),("ND", "North Dakota"),("MP", "Northern Mariana Islands"),("OH", "Ohio"),
    ("OK", "Oklahoma"),("OR", "Oregon"),("PW", "Palau"),("PA", "Pennsylvania"),("PR", "Puerto Rico"),
    ("RI", "Rhode Island"),("SC", "South Carolina"),("SD", "South Dakota"),("TN", "Tennessee"),
    ("TX", "Texas"),("UT", "Utah"),("VT", "Vermont"),("VI", "Virgin Islands"),("VA", "Virginia"),
    ("WA", "Washington"),("WV", "West Virginia"),("WI", "Wisconsin"),("WY", "Wyoming"),
)
class Address(models.Model):
    contact=models.CharField(max_length=50)
    address1=models.CharField(max_length=200)
    address2=models.CharField(max_length=50,blank=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=30,choices=STATES)
    zipCode=models.CharField(max_length=12)
    phone=models.CharField(max_length=15,blank=True)
    class Meta:
        abstract=True

class Partsinv(models.Model):
    item = models.CharField(db_column='Item', blank=True, null=True,max_length=100)  # Field name made lowercase.
    number = models.CharField(primary_key=True,max_length=20,blank=True)
    group_id = models.CharField(db_column='Group_ID', blank=True, null=True,max_length=100)  # Field name made lowercase.
    class_id = models.CharField(db_column='Class_ID', blank=True, null=True,max_length=100)  # Field name made lowercase.
    inventory = models.IntegerField(db_column='Inventory', blank=True, null=True)  # Field name made lowercase.
    low_inv = models.IntegerField(blank=True)
    high_inv = models.IntegerField(blank=True)
    location = models.CharField(max_length=20,blank=True)
    def __str__(self):
        return self.number

    class Meta:
        managed = False
        db_table = 'partsinv'

class CheckForm(ModelForm):
    class Meta:
        model = Partsinv
        fields=['number']
class TimeRecord(models.Model):
    ref=models.IntegerField()
    call=models.DateTimeField()
    pre_diagnosis=models.DateTimeField()
    tech=models.DateTimeField()
    part=models.DateTimeField()
class UnitBasicInfo(models.Model):
    businessName=models.CharField(max_length=100)
    contactName=models.CharField(max_length=50)
    serialNumber=models.CharField(max_length=50)
    phone=models.CharField(max_length=15,null=True)
    email=models.EmailField(null=True,blank=True)
    business_hour=models.CharField(max_length=80,null=True,blank=True)
    location_add1=models.CharField(max_length=200)
    location_add2=models.CharField(max_length=200,null=True,blank=True)
    location_city=models.CharField(max_length=20)
    location_state=models.CharField(max_length=30)
    location_zip=models.IntegerField()
    tech_add1=models.CharField(max_length=200,null=True,blank=True)
    tech_add2=models.CharField(max_length=200,null=True,blank=True)
    tech_city=models.CharField(max_length=20,null=True,blank=True)
    tech_state=models.CharField(max_length=30,null=True,blank=True)
    tech_zip=models.IntegerField(null=True,blank=True)
    issue=models.TextField()
    warranty=models.NullBooleanField(null=True,blank=True)
    warrantyNote=models.TextField(null=True,blank=True)
    tsq=models.TextField(null=True,blank=True)
    techName=models.CharField(max_length=100,null=True,blank=True)
    techPhone=models.CharField(max_length=15,null=True,blank=True)
    techEmail=models.EmailField(null=True,blank=True)
    scheDate=models.DateField(null=True,blank=True)
    techNote=models.TextField(null=True,blank=True)
    callTime=models.DateTimeField(auto_now_add=True)
    receiver=models.CharField(max_length=50)
    areaCode=models.IntegerField(default=0)
    sksid=models.CharField(max_length=20,null=True,blank=True)
    finished=models.BooleanField(default=False)
    pre_diagnosis=models.TextField(null=True,blank=True)
    pre_diagnosis_flag=models.BooleanField(blank=True,default=False)
    followup_customer=models.TextField(null=True,blank=True)
    followup_customer_time=models.DateTimeField(null=True,auto_now=True)
    followup_tech=models.TextField(null=True,blank=True)
    followup_tech_time=models.DateTimeField(null=True,auto_now=True)
    def __str__(self):
        return self.serialNumber

class PartRequest(models.Model):
    sn=models.CharField(max_length=30,null=True,blank=True)
    sksid=models.CharField(max_length=30)
    contact=models.CharField(max_length=50)
    number=models.CharField(max_length=30)
    name=models.CharField(max_length=70)
    code=models.IntegerField()
    shipping_method=models.CharField(max_length=20,choices=SHIPPING_METHOD,blank=True)
    qty=models.IntegerField()
    request_time=models.DateField(auto_now_add=True)
    tracking=models.CharField(max_length=50,null=True,blank=True)
    approved=models.BooleanField(default=False)
    location_add1=models.CharField(max_length=200)
    location_add2=models.CharField(max_length=200,null=True,blank=True)
    location_city=models.CharField(max_length=20)
    location_state=models.CharField(max_length=30)
    location_zip=models.IntegerField()
    pre_diagnosis=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.sksid
