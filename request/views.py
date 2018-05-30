import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import CheckForm, Partsinv, UnitBasicInfo, PartRequest
from django.utils import timezone
from .forms import BasicForm, RequestForm, BasicInfoForm, HotTechQuestionForm, ColdTechQuestionForm, DispatchForm, PreDiagnosisForm,PartForm,PartRequestUpdateForm

def request_part(request,pk):
    form=PartForm()
    unit=get_object_or_404(UnitBasicInfo, pk=pk)
    sksid=unit.sksid
    return render(request, 'request/part_request.html',{'form': form,'id':sksid})
def show_part_list(request):
    part = PartRequest.objects.all()
    return render(request, 'request/part_request_list.html', {'request':part})
def show_part_detail(request,pk):
    part = get_object_or_404(PartRequest, pk=pk)
    form=PartRequestUpdateForm()
    return render(request, 'request/part_request_detail.html', {'part': part,'form':form})
def update_part(request,pk):
    if request.method == "POST":
        form = PartForm(request.POST)
        if form.is_valid():
            unit=get_object_or_404(UnitBasicInfo, pk=pk)
            sksid=unit.sksid
            new_part_request=PartRequest()
            new_part_request.sksid=sksid
            contact=""
            add1=""
            add2=""
            city=""
            state=""
            zip=""
            if request.POST["to_customer"]:
                contact=unit.contactName
                add1=unit.location_add1
                add2=unit.location_add2
                city=unit.location_city
                state=unit.location_state
                zip=unit.location_zip
            else:
                contact=form.cleaned_data["contact"]
                add1=form.cleaned_data["address1"]
                add2=form.cleaned_data["address2"]
                city=form.cleaned_data["city"]
                state=form.cleaned_data["state"]
                zip=form.cleaned_data["zip"]
            new_part_request.contact=contact
            new_part_request.location_add1=add1
            new_part_request.location_add2=add2
            new_part_request.location_city=city
            new_part_request.location_state=state
            new_part_request.location_zip=zip
            n1=form.cleaned_data["number1"]
            m1=form.cleaned_data["name1"]
            q1=form.cleaned_data["qty1"]
            new_part_request.number=n1
            new_part_request.name=m1
            new_part_request.qty=int(q1)
            new_part_request.save()
            n2=form.cleaned_data["number2"]
            m2=form.cleaned_data["name2"]
            q2=form.cleaned_data["qty2"]
            n3=form.cleaned_data["number3"]
            m3=form.cleaned_data["name3"]
            q3=form.cleaned_data["qty3"]
            if n2!="" and q2!="" and m2!="":
                new_part_request=PartRequest()
                new_part_request.sksid=sksid
                new_part_request.contact=contact
                new_part_request.location_add1=add1
                new_part_request.location_add2=add2
                new_part_request.location_city=city
                new_part_request.location_state=state
                new_part_request.location_zip=zip
                new_part_request.number=n2
                new_part_request.name=m2
                new_part_request.qty=int(q2)
                new_part_request.save()
            if n3!="" and q3!="" and m3!="":
                new_part_request=PartRequest()
                new_part_request.sksid=sksid
                new_part_request.contact=contact
                new_part_request.location_add1=add1
                new_part_request.location_add2=add2
                new_part_request.location_city=city
                new_part_request.location_state=state
                new_part_request.location_zip=zip
                new_part_request.number=n3
                new_part_request.name=m3
                new_part_request.qty=int(q3)
                new_part_request.save()
            return redirect("/user/dispatcher/")
def update_part_request(request,pk):
    if request.method == "POST":
        form=PartRequestUpdateForm(request.POST)
        if form.is_valid():
            part = PartRequest.objects.get(pk=pk)
            tracking=form.cleaned_data["tracking"]
            note = form.cleaned_data["note"]
            part.tracking=tracking
            part.tracking=note
            part.save()
            return redirect('/request/part/')
def basic_info(request):
    form=BasicForm()
    return render(request, 'request/base.html',{'form': form})

def get_all_undiagnosed(request):
    all=UnitBasicInfo.objects.filter(pre_diagnosis=None)
    return render(request, 'request/pre_diagnosis_list.html', {'requests':all})
def get_detail_undiagnosed(request,pk):
    unit = get_object_or_404(UnitBasicInfo, pk=pk)
    form=PreDiagnosisForm()
    return render(request, 'request/pre_diagnosis_detail.html', {'unit': unit,'form':form})
def update_diagnosis(request,pk):
    if request.method == "POST":
        form=PreDiagnosisForm(request.POST)
        if form.is_valid():
            note=form.cleaned_data["note"]
            unit=get_object_or_404(UnitBasicInfo, pk=pk)
            unit.pre_diagnosis=note
            unit.save()
            return redirect('/request/pre_diagnosis')
def show_tech_question_page(request):
    if request.method == "POST":
        form = BasicForm(request.POST)
        if form.is_valid():
            name_business=form.cleaned_data["businessName"]
            name_contact=form.cleaned_data["contactName"]
            serial=form.cleaned_data["serialNumber"]
            phone=form.cleaned_data["phoneCustomer"]
            email=form.cleaned_data["emailAddress"]
            add1=form.cleaned_data["add1"]
            add2=form.cleaned_data["add2"]
            city=form.cleaned_data["city"]
            state=form.cleaned_data["state"]
            zip=form.cleaned_data["zip"]
            issue=form.cleaned_data["issue"]
            unit_type=form.cleaned_data["type"]
            request.session["unit_type"]=unit_type
            request.session["unit_sn"]=serial
            new_unit=UnitBasicInfo()
            new_unit.businessName=name_business
            new_unit.contactName=name_contact
            new_unit.serialNumber=serial
            new_unit.phone=phone
            new_unit.email=email
            new_unit.location_add1=add1
            new_unit.location_add2=add2
            new_unit.location_city=city
            new_unit.location_state=state
            new_unit.location_zip=zip
            new_unit.issue=issue
            new_unit.receiver=request.session['user_name']
            new_unit.save()
            if request.session['unit_type']=="HOT":
                form=HotTechQuestionForm()
                return render(request, 'request/tech_question_hot.html', {'form':form})
            elif request.session['unit_type']=="COLD":
                form=ColdTechQuestionForm()
                return render(request, 'request/tech_question_cold.html', {'form':form})
            else:
                redirect('/user')
def update_hot(request):
    if request.method == "POST":
        form = HotTechQuestionForm(request.POST)
        if form.is_valid():
            tsq1=form.cleaned_data["pilot_light"]
            tsq2=form.cleaned_data["pilot_stay"]
            tsq3=form.cleaned_data["burner_light"]
            tsq=("The pilot can be lighted on: "+tsq1+"<br>"
                +"The pilot can stay on: "+tsq2+"<br>"
                +"The burner can be turned on: "+tsq3
                )
            unit=UnitBasicInfo.objects.get(serialNumber=request.session['unit_sn'])
            unit.tsq=tsq
            unit.save()
    return redirect('/user')
def update_cold(request):
    if request.method == "POST":
        form = ColdTechQuestionForm(request.POST)
        if form.is_valid():
            tsq1=form.cleaned_data["filter"]
            tsq2=form.cleaned_data["displayTemp"]
            tsq3=form.cleaned_data["realTemp"]
            tsq4=form.cleaned_data["controller"]
            tsq5=form.cleaned_data["snowflake"]
            tsq6=form.cleaned_data["fan"]
            tsq7=form.cleaned_data["iceEvap"]
            tsq8=form.cleaned_data["condFan"]
            tsq9=form.cleaned_data["evapFan"]
            tsq10=form.cleaned_data["comp"]
            tsq=("Filter Clean: "+tsq1+"\n"+"Display Temperature: "+str(tsq2)+"\n"+"Real Temperature: "+str(tsq3)+"\n"
                +"Controller: "+tsq4+"\n"+"Snowflake Icon: "+tsq5+"\n"+"Fan Icon: "+tsq6+"\n"
                +"Ice on Evap: "+tsq7+"\n"+"Cond Fan Running: "+tsq8+"\n"+"Evap Fan Running: "+tsq9+"\n"
                +"Compressor running: "+tsq10+"\n")
            unit=UnitBasicInfo.objects.get(serialNumber=request.session['unit_sn'])
            unit.tsq=tsq
            unit.save()
    return redirect('/user')
def submit(request):
    if request.method == "POST":
        form = BasicInfoForm(request.POST)
        if form.is_valid():
            name_business=form.cleaned_data["businessName"]
            name_contact=form.cleaned_data["contactName"]
            serial=form.cleaned_data["serialNumber"]
            phone=form.cleaned_data["phoneCustomer"]
            email=form.cleaned_data["emailAddress"]
            add1=form.cleaned_data["add1"]
            add2=form.cleaned_data["add2"]
            city=form.cleaned_data["city"]
            state=form.cleaned_data["state"]
            zip=form.cleaned_data["zip"]
            issue=form.cleaned_data["issue"]
            tsq1=form.cleaned_data["filter"]
            tsq2=form.cleaned_data["displayTemp"]
            tsq3=form.cleaned_data["realTemp"]
            tsq4=form.cleaned_data["controller"]
            tsq5=form.cleaned_data["snowflake"]
            tsq6=form.cleaned_data["fan"]
            tsq7=form.cleaned_data["iceEvap"]
            tsq8=form.cleaned_data["condFan"]
            tsq9=form.cleaned_data["evapFan"]
            tsq10=form.cleaned_data["comp"]
            tsq=("Filter Clean: "+tsq1+"\n"+"Display Temperature: "+str(tsq2)+"\n"+"Real Temperature: "+str(tsq3)+"\n"
                +"Controller: "+tsq4+"\n"+"Snowflake Icon: "+tsq5+"\n"+"Fan Icon: "+tsq6+"\n"
                +"Ice on Evap: "+tsq7+"\n"+"Cond Fan Running: "+tsq8+"\n"+"Evap Fan Running: "+tsq9+"\n"
                +"Compressor running: "+tsq10+"\n")

            new_unit=UnitBasicInfo()
            new_unit.businessName=name_business
            new_unit.contactName=name_contact
            new_unit.serialNumber=serial
            new_unit.phone=phone
            new_unit.email=email
            new_unit.location_add1=add1
            new_unit.location_add2=add2
            new_unit.location_city=city
            new_unit.location_state=state
            new_unit.location_zip=zip
            new_unit.issue=issue
            new_unit.tsq=tsq
            new_unit.receiver=request.session['user_name']
            new_unit.save()
        return redirect('/request/allService')
    else:
        form = BasicInfoForm()

def available(request):
    form=CheckForm()
    return render(request, 'request/check.html',{'form': form})

def submita(request):

    form = CheckForm(request.POST)
    query = request.POST.get('number','0')
    result=Partsinv.objects.get(number=query)
    return render(request, 'request/availability.html', {'request':result})

def showAllService(request):
    request_list = UnitBasicInfo.objects.order_by('-callTime')
    return render(request, 'request/allService.html', {'request':request_list})
def showAllRequests(request):
    request_list = Request.objects.order_by('-requestTime')
    return render(request, 'request/request_detail.html', {'request':request_list})

def showPendingRequests(request):
    request_list = Request.objects.filter(requestStatue=False)
    return render(request, 'request/request_detail.html', {'request':request_list})

def showFinishedRequests(request):
    request_list = Request.objects.filter(requestStatue=True)
    return render(request, 'request/request_detail.html', {'request':request_list})
