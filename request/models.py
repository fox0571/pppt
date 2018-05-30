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

class UnitBasicInfo(models.Model):
    businessName=models.CharField(max_length=100)
    contactName=models.CharField(max_length=50)
    serialNumber=models.CharField(max_length=50)
    phone=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    location_add1=models.CharField(max_length=200)
    location_add2=models.CharField(max_length=200,null=True)
    location_city=models.CharField(max_length=20)
    location_state=models.CharField(max_length=30)
    location_zip=models.IntegerField()
    issue=models.TextField()
    warranty=models.NullBooleanField(null=True)
    warrantyNote=models.CharField(max_length=100,null=True,blank=True)
    tsq=models.TextField(null=True)
    techName=models.CharField(max_length=50,null=True)
    techPhone=models.IntegerField(null=True)
    techEmail=models.EmailField(null=True)
    scheDate=models.DateField(null=True)
    techNote=models.CharField(max_length=200,null=True)
    callTime=models.DateTimeField(auto_now_add=True)
    receiver=models.CharField(max_length=50)
    areaCode=models.IntegerField(default=0)
    sksid=models.CharField(max_length=20,null=True)
    finished=models.BooleanField(default=False)
    pre_diagnosis=models.TextField(null=True)

    def __str__(self):
        return self.serialNumber

class PartRequest(models.Model):
    sksid=models.CharField(max_length=30)
    contact=models.CharField(max_length=50)
    number=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    code=models.IntegerField()
    shipping_method=models.CharField(max_length=20,choices=SHIPPING_METHOD,blank=True)
    qty=models.IntegerField()
    request_time=models.DateField(auto_now_add=True)
    tracking=models.CharField(max_length=50,null=True,blank=True)
    approved=models.BooleanField(default=False)
    location_add1=models.CharField(max_length=200)
    location_add2=models.CharField(max_length=200,null=True)
    location_city=models.CharField(max_length=20)
    location_state=models.CharField(max_length=30)
    location_zip=models.IntegerField()
    def __str__(self):
        return self.sksid
