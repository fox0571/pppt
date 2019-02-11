from .models import UnitBasicInfo, PartRequest
from units.models import Part
from warranty.models import Invoice
import re

uall=UnitBasicInfo.objects.all()
pall=PartRequest.objects.filter(part=None)
ptall=Part.objects.all()
def update():
    for p in pall:
        number=re.sub('[!()@#*$&%^]','',p.number)
        try:
            part=ptall.get(number=number)
            print(p.number,part.number)
            p.part=part
            p.save()
        except Part.DoesNotExist:
            print("NOT FOUND",p.number,p.name)

iall=Invoice.objects.all()
def update_invoice_type():
    count=0
    for i in iall:
        if i.status == 3:
            i.status = 0
            i.invoice_type = 1
            count=count+1
            print(i.invoice,i.incident)
            i.save()
    print("total count",count)
            

