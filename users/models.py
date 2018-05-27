from django.db import models

# Create your models here.
class Users(models.Model):
    GROUPS=(
    ("dispathcer","DISPATCHER"),
    ("operator","OPERATOR"),
    ("warranty","WARRANTY"),
    ("admin","ADMIN"),
    )
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    tasks=models.IntegerField()
    group=models.CharField(max_length=15,choices=GROUPS,default="operator")
