from django.db import models

# Create your models here.
class Users(models.Model):
    GROUPS=(
        ("dispatcher","DISPATCHER"),
        ("operator","OPERATOR"),
        ("warranty","WARRANTY"),
        ("parts","PARTS"),
        ("adminop","ADMIN_OP"),
        ("admindp","ADMIN_DP"),
        ("admin","ADMIN"),
        ("account","ACCOUNT")
    )
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    current_month = models.IntegerField(default=1)
    current_tasks = models.IntegerField(default=0)
    total_tasks=models.IntegerField(default=0)
    group=models.CharField(max_length=15,choices=GROUPS,default="operator")

    def __str__(self):
        return self.name
