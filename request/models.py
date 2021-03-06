from django.db import models
from django.forms import ModelForm
from taggit.managers import TaggableManager
from units.models import Unit, Part
from django.contrib.auth.models import User

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
CHOICES_8=(
    (False, 'To 3rd party tech company'),
    (True, 'To in-house tech dispatcher'),
)
CHOICES_0=(
    (1, 'PO'),
    (2, 'WARRANTY'),
)
class Address(models.Model):
    contact=models.CharField(max_length=50)
    address1=models.CharField(max_length=190)
    address2=models.CharField(max_length=50,blank=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=30,choices=STATES)
    zipCode=models.CharField(max_length=12)
    phone=models.CharField(max_length=15,blank=True)
    class Meta:
        abstract=True
class Tech(models.Model):
    business = models.CharField(max_length=100)
    contact=models.CharField(max_length=50)
    phone=models.CharField(max_length=15,null=True)
    email=models.EmailField(null=True,blank=True)
    address1=models.CharField(max_length=190)
    address2=models.CharField(max_length=50,blank=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=30,choices=STATES)
    zip=models.CharField(max_length=12)
    phone=models.CharField(max_length=15,blank=True)

    def __str__(self):
        return self.contact+" - "+self.business
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
    model = models.ForeignKey(Unit, on_delete=models.CASCADE,null=True,blank=True)
    phone=models.CharField(max_length=15,null=True)
    email=models.EmailField(null=True,blank=True)
    business_hour=models.CharField(max_length=80,null=True,blank=True)
    location_add1=models.CharField(max_length=190)
    location_add2=models.CharField(max_length=190,null=True,blank=True)
    location_city=models.CharField(max_length=20)
    location_state=models.CharField(max_length=30)
    location_zip=models.CharField(max_length=20)
    tech_add1=models.CharField(max_length=190,null=True,blank=True)
    tech_add2=models.CharField(max_length=190,null=True,blank=True)
    tech_city=models.CharField(max_length=20,null=True,blank=True)
    tech_state=models.CharField(max_length=30,null=True,blank=True)
    tech_zip=models.CharField(max_length=20,null=True,blank=True)
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
    #receiver=models.CharField(max_length=50)
    create_user = models.ForeignKey(User, related_name="creater",on_delete=models.CASCADE,null=True,blank=True)
    dispatcher = models.ForeignKey(User, related_name="dispatcher",on_delete=models.CASCADE,null=True,blank=True)
    areaCode=models.IntegerField(default=0)
    sksid=models.CharField(max_length=20,null=True,blank=True)
    finished=models.BooleanField(default=False)
    pre_diagnosis=models.TextField(null=True,blank=True)
    pre_diagnosis_flag=models.BooleanField(blank=True,default=False)
    timestamp_diagnosis=models.DateTimeField(blank=True,null=True)
    pre_diagnosis_pending=models.BooleanField(default=False,blank=True)
    long_term_pending = models.BooleanField(default=False,blank=True)
    followup_customer=models.TextField(null=True,blank=True)
    followup_customer_time=models.DateTimeField(null=True,auto_now=True)
    followup_tech=models.TextField(null=True,blank=True)
    followup_tech_time=models.DateTimeField(null=True,auto_now=True)
    inhouse = models.BooleanField(default=False,choices=CHOICES_8)
    replacement = models.BooleanField(default=False)
    prefer_reached = models.CharField(max_length=90,default="by phone")

    def __str__(self):
        #return self.serialNumber
        if self.sksid:
            return self.sksid+"-"+self.serialNumber
        else:
            return self.serialNumber

    class Meta:
        ordering = ('sksid',)

class PartRequest(models.Model):
    sn=models.CharField(max_length=70,null=True,blank=True)
    sksid=models.CharField(max_length=30,null=True)
    contact=models.CharField(max_length=100)
    number=models.CharField(max_length=30)
    name=models.CharField(max_length=70)
    code=models.IntegerField()
    shipping_method=models.CharField(max_length=20,choices=SHIPPING_METHOD,blank=True)
    qty=models.IntegerField()
    request_time=models.DateField(auto_now_add=True)
    tracking=models.CharField(max_length=50,null=True,blank=True)
    note = models.TextField(null=True,blank=True)
    approved=models.BooleanField(default=False)
    location_add1=models.CharField(max_length=190)
    location_add2=models.CharField(max_length=190,null=True,blank=True)
    location_city=models.CharField(max_length=20)
    location_state=models.CharField(max_length=30)
    location_zip=models.CharField(max_length=20)
    pre_diagnosis=models.TextField(null=True,blank=True)
    part_type=models.IntegerField(choices=CHOICES_0,default=2,blank=True)
    case = models.ForeignKey(UnitBasicInfo, on_delete=models.CASCADE,null=True)
    part = models.ForeignKey(Part, on_delete=models.CASCADE,null=True)
    created_by = models.ForeignKey(User, related_name="part_creater",on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.sksid+','+self.number

    class Meta:
        ordering = ('number',)
        permissions = (
            ("change_part_status", "Can change the status of part request"),
        )

class Tag(models.Model):
    name = models.CharField(max_length=70,blank=True)
    name_chn = models.CharField(max_length=100,blank=True,null=True)
    model = models.ManyToManyField(UnitBasicInfo)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ('name',)

class FileSimpleModel(models.Model):
    incident = models.ForeignKey(UnitBasicInfo, on_delete=models.CASCADE,null=True,blank=True)
    file_field = models.FileField(upload_to="%Y/%m/%d/")
