import datetime
from django.shortcuts import render, redirect, get_object_or_404
from .models import UnitBasicInfo, PartRequest
from django.utils import timezone
from .forms import FirstForm, RequestForm, DiagnosisForm, HotTechQuestionForm, ColdTechQuestionForm, PreDiagnosisForm,PartForm,PartRequestUpdateForm
from users.forms import DispatchForm
from django.views.generic import View
from .render import Render
from warranty.models import Invoice
OPERATOR_GROUP=["Anna","Bradon","Jackie","Randi"]

class Pdf(View):
    def get(self, request,pk):
        unit=get_object_or_404(UnitBasicInfo, pk=pk)
        inv=Invoice.objects.all().filter(sksid=unit.sksid)
        params = {
            'unit':unit,
            'invoices':inv,
        }
        return Render.render('account/print_page.html', params)
class Pdf_work_order(View):
    def get(self, request,pk):
        unit=get_object_or_404(UnitBasicInfo, pk=pk)
        params = {
            'unit':unit,
        }
        return Render.render('dispatcher/pdf.html', params)
def get_order(request,pk):
    unit=get_object_or_404(UnitBasicInfo, pk=pk)
    return render(request, 'dispatcher/order.html', {'unit':unit})
def update_statue(request,pk):
    unit=get_object_or_404(UnitBasicInfo, pk=pk)
    if request.method == "POST":
        statue=request.POST.get("statue","")
        if statue=="finished":
            unit.finished=True
        else:
            unit.finished=False
        unit.save()
        return redirect('/user/dispatcher/scheduled/')
    return render(request, 'dispatcher/statue.html', {'unit':unit})
def update_follow_tech(request,pk):
    if request.method == "POST":
        note=request.POST.get("tech","")
        note=str(datetime.datetime.now(tz=None))+"\n"+note
        unit=get_object_or_404(UnitBasicInfo, pk=pk)
        if unit.followup_tech:
            unit.followup_tech=unit.followup_tech+"\n"+note
        else:
            unit.followup_tech=note
        unit.save()
    return render(request, 'dispatcher/followup.html', {'unit': unit})
def update_follow_customer(request,pk):
    if request.method == "POST":
        note=request.POST.get("customer","")
        note=str(datetime.datetime.now(tz=None))+"\n"+note
        unit=get_object_or_404(UnitBasicInfo, pk=pk)
        if unit.followup_customer:
            unit.followup_customer=unit.followup_customer+"\n"+note
        else:
            unit.followup_customer=note
        unit.save()
    return render(request, 'dispatcher/followup.html', {'unit': unit})
def show_detail(request,pk):
    unit = get_object_or_404(UnitBasicInfo, pk=pk)
    id=unit.sksid
    parts = PartRequest.objects.all().filter(sksid=id)
    para={
        'unit':unit,
        'parts':parts,
    }
    return render(request,'request/detail.html',para)
def part_dashboard(request):
    new=PartRequest.objects.all().filter(tracking=None).count()
    all=PartRequest.objects.all().count()
    para={
        "new":new,
        "all":all,
    }
    return render(request, 'part/dashboard.html',para)
def show_part_list(request):
    part = PartRequest.objects.all()
    return render(request, 'part/list.html', {'request':part})
def show_new_part(request):
    part = PartRequest.objects.all().filter(tracking=None).order_by('location_add1')
    return render(request, 'request/part_request_list.html', {'request':part})
def show_part_detail(request,pk):
    part = get_object_or_404(PartRequest, pk=pk)
    form=PartRequestUpdateForm()
    return render(request, 'request/part_request_detail.html', {'part': part,'form':form})
def update_part(request,pk):
    form=PartForm()
    unit=get_object_or_404(UnitBasicInfo, pk=pk)
    sksid=unit.sksid
    parts=PartRequest.objects.all().filter(sksid=sksid)
    add=""
    if parts.count()!=0:
        p=parts[0]
        add2=""
        if p.location_add2:
            add2=p.location_add2
        add=p.location_add1+" "+add2+', '+p.location_city+" "+p.location_state
    if request.method == "POST":

        form = PartForm(request.POST)
        if form.is_valid():
            print("test")
            new_part_request=PartRequest()
            new_part_request.sksid=sksid
            contact=""
            add1=""
            add2=""
            city=""
            state=""
            zip=""
            new_part_request.pre_diagnosis=unit.pre_diagnosis
            if request.POST.get('to_customer', False):
                contact=unit.contactName
                add1=unit.location_add1
                if unit.location_add2:
                    add2=unit.location_add2
                city=unit.location_city
                state=unit.location_state
                zip=unit.location_zip
            elif request.POST.get('to_tech', False):
                contact=unit.techName
                add1=unit.tech_add1
                if unit.tech_add2:
                    add2=unit.tech_add2
                city=unit.tech_city
                state=unit.tech_state
                zip=unit.tech_zip
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
            new_part_request.code=unit.areaCode
            new_part_request.sn=unit.serialNumber
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
                new_part_request.code=unit.areaCode
                new_part_request.pre_diagnosis=unit.pre_diagnosis
                new_part_request.sn=unit.serialNumber
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
                new_part_request.code=unit.areaCode
                new_part_request.pre_diagnosis=unit.pre_diagnosis
                new_part_request.sn=unit.serialNumber
                new_part_request.save()
            return redirect("#/")
        return render(request, 'request/part_request.html',{'form': form,'parts':parts,'unit':unit,'add':add})
    return render(request, 'request/part_request.html',{'form': form,'parts':parts,'unit':unit,'add':add})
def update_part_request(request,pk):
    if request.method == "POST":
        form=PartRequestUpdateForm(request.POST)
        if form.is_valid():
            part = PartRequest.objects.get(pk=pk)
            tracking=form.cleaned_data["tracking"]
            note = form.cleaned_data["note"]
            part.tracking=tracking
            part.note=note
            part.save()
            return redirect('/request/part/')
def edit_basic(request,pk):
    unit=get_object_or_404(UnitBasicInfo, pk=pk)
    pre_sn=unit.serialNumber
    if request.method == "POST":
        form = FirstForm(request.POST, instance=unit)
        if form.is_valid():
            sn=form.cleaned_data["serialNumber"]
            if sn != pre_sn:
                unit.warranty=None
            unit = form.save()
            unit_type=form.cleaned_data["type"]
            sn=form.cleaned_data["type"]
            request.session["unit_type"]=unit_type
            if request.session['unit_type']=="HOT":
                form=HotTechQuestionForm()
                return render(request, 'request/tech_question_hot.html', {'form':form,'unit':unit})
            elif request.session['unit_type']=="COLD":
                form=ColdTechQuestionForm()
                return render(request, 'request/tech_question_cold.html', {'form':form,'unit':unit})
            return redirect('/user/operator/')
    else:
        form = FirstForm(instance=unit)
    return render(request, 'operator/basic_edit.html', {'form':form,'unit':unit,'pk':unit.pk})
def update_basic(request):
    form=FirstForm()
    if request.method == "POST":
        form = FirstForm(request.POST)
        if form.is_valid():
            new_unit=form.save(commit=False)
            unit_type=form.cleaned_data["type"]
            request.session["unit_type"]=unit_type
            new_unit.receiver=request.session['user_name']
            new_unit.save()
            if request.session['unit_type']=="HOT":
                form=HotTechQuestionForm()
                return render(request, 'request/tech_question_hot.html', {'form':form,'unit':new_unit})
            elif request.session['unit_type']=="COLD":
                form=ColdTechQuestionForm()
                return render(request, 'request/tech_question_cold.html', {'form':form,'unit':new_unit})
            return redirect('/user/operator/')
        return render(request, 'operator/basic.html',{'form': form})
    return render(request, 'operator/basic.html',{'form': form})
def show_admindp(request):
    all=UnitBasicInfo.objects.filter(warranty=True).filter(pre_diagnosis_flag=False).filter(pre_diagnosis_pending=False)
    alls=UnitBasicInfo.objects.filter(warranty=True).count()
    new=all.count()
    pending=UnitBasicInfo.objects.filter(pre_diagnosis_pending=True).count()
    return render(request, 'dispatcher/admin.html', {'new':new,'all':alls,'pending':pending})
def get_all_undiagnosed(request):
    all=UnitBasicInfo.objects.filter(warranty=True).filter(pre_diagnosis_flag=False).filter(pre_diagnosis_pending=False)
    return render(request, 'request/pre_diagnosis_list.html', {'requests':all})
def get_all_pending_undiagnosed(request):
    all=UnitBasicInfo.objects.filter(warranty=True).filter(pre_diagnosis_pending=True)
    return render(request, 'request/pre_diagnosis_list.html', {'requests':all})
def get_all_diag(request):
    all=UnitBasicInfo.objects.filter(warranty=True).order_by("-timestamp_diagnosis")
    return render(request, 'request/pre_diagnosis_list.html', {'requests':all})
def show_adminop(request):
    all=UnitBasicInfo.objects.filter(warranty=True).filter(pre_diagnosis_flag=False)
    new=all.count()
    final_data = []
    today = datetime.date.today()
    delta= datetime.timedelta(today.weekday())
    start = today-delta
    print(start)
    for user in OPERATOR_GROUP:
        count = UnitBasicInfo.objects.filter(receiver=user).filter(
            callTime__gte=start).count()
        final_data.append(count)
    return render(request, 'request/operator_supervisor.html', {'new':new,'data':final_data})
def diagnosis(request,pk):
    unit = get_object_or_404(UnitBasicInfo, pk=pk)
    if request.method == "POST":
        form=DiagnosisForm(request.POST,instance=unit)
        if form.is_valid():
            unit=form.save(commit=False)
            print (unit.pre_diagnosis_pending)
            if not unit.pre_diagnosis_pending:
                unit.timestamp_diagnosis=datetime.datetime.now()
                unit.pre_diagnosis_flag=True
                unit.save()
            else:
                unit.pre_diagnosis_pending=True
                unit.save()
            return redirect('/request/diag')
    else:
        form=DiagnosisForm(instance=unit)
    return render(request, 'request/pre_diagnosis_detail.html', {'unit': unit,'form':form})
def update_tech_info(request,pk):
    unit = get_object_or_404(UnitBasicInfo, pk=pk)
    form=DispatchForm()
    if request.method == "POST":
        form=DispatchForm(request.POST)
        if form.is_valid():
            tech_name=form.cleaned_data["tech_name"]
            tech_phone=form.cleaned_data["tech_phone"]
            tech_email=form.cleaned_data["tech_email"]
            tech_note=form.cleaned_data["tech_note"]
            tech_add1 = form.cleaned_data["tech_add1"]
            tech_add2 = form.cleaned_data["tech_add2"]
            tech_city = form.cleaned_data["tech_city"]
            tech_state = form.cleaned_data["tech_state"]
            tech_zip = form.cleaned_data["tech_zip"]
            schedule_time=form.cleaned_data["schedule_time"]
            unit=get_object_or_404(UnitBasicInfo, pk=pk)
            unit.techName=tech_name
            unit.techPhone=tech_phone
            unit.techEmail=tech_email
            unit.scheDate=schedule_time
            unit.tech_add1=tech_add1
            unit.tech_add2=tech_add2
            unit.tech_city=tech_city
            unit.tech_state=tech_state
            unit.tech_zip=tech_zip
            a_note=("Scheduled Time: "+str(schedule_time)+"\n"
                    +"Name: "+str(tech_name)+"\n"
                    +"Phone: "+str(tech_phone)+"\n"
                    +"Email: "+tech_email+"\n"
                    +"Note: "+str(tech_note)+"\n"
                    +"Location: "+tech_add1+" "+tech_add2+" "+tech_city+" "+tech_state+"\n"
                    )
            if unit.techNote:
                unit.techNote=unit.techNote+"\n"+a_note
            else:
                unit.techNote=a_note
            unit.save()
    return render(request, 'dispatcher/tech.html', {'unit': unit,'form':form})
def show_question(request,pk):
    if request.session['unit_type']=="HOT":
        form=HotTechQuestionForm()
        return render(request, 'request/tech_question_hot.html', {'form':form,'unit':new_unit})
    elif request.session['unit_type']=="COLD":
        form=ColdTechQuestionForm()
        return render(request, 'request/tech_question_cold.html', {'form':form,'unit':new_unit})
    else:
        redirect('/user')
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
                return render(request, 'request/tech_question_hot.html', {'form':form,'unit':new_unit})
            elif request.session['unit_type']=="COLD":
                form=ColdTechQuestionForm()
                return render(request, 'request/tech_question_cold.html', {'form':form,'unit':new_unit})
            else:
                redirect('/user')
def update_hot(request,pk):
    unit=UnitBasicInfo.objects.get(pk=pk)
    form=HotTechQuestionForm()
    if request.method == "POST":
        form = HotTechQuestionForm(request.POST)
        if form.is_valid():
            tsq1=form.cleaned_data["pilot_light"]
            tsq2=form.cleaned_data["pilot_stay"]
            tsq3=form.cleaned_data["burner_light"]
            tsq=("The pilot can be lighted on: "+tsq1+"\n"
                +"The pilot can stay on: "+tsq2+"\n"
                +"The burner can be turned on: "+tsq3
                )
            unit=UnitBasicInfo.objects.get(pk=pk)
            unit.tsq=tsq
            unit.save()
            return redirect('/user')
        return render(request, 'request/tech_question_hot.html', {'form':form,'unit':unit})
    return render(request, 'request/tech_question_hot.html', {'form':form,'unit':unit})
def update_cold(request,pk):
    unit=UnitBasicInfo.objects.get(pk=pk)
    form=ColdTechQuestionForm()
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
            tsq11=form.cleaned_data["door"]
            tsq=("Filter Clean: "+tsq1+"\n"+"Display Temperature: "+str(tsq2)+"\n"+"Real Temperature: "+str(tsq3)+"\n"
                +"Controller: "+tsq4+"\n"+"Snowflake Icon: "+tsq5+"\n"+"Fan Icon: "+tsq6+"\n"
                +"Ice on Evap: "+tsq7+"\n"+"Cond Fan Running: "+tsq8+"\n"+"Evap Fan Running: "+tsq9+"\n"
                +"Compressor running: "+tsq10+"\n"+"Door issue: "+tsq11+"\n")
            unit.tsq=tsq
            unit.save()
            return redirect('/user')
        return render(request, 'request/tech_question_cold.html', {'form':form,'unit':unit})
    return render(request, 'request/tech_question_cold.html', {'form':form,'unit':unit})
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
    request_list = UnitBasicInfo.objects.order_by('-callTime')
    return render(request, 'request/all_records.html', {'request':request_list})

def showPendingRequests(request):
    request_list = Request.objects.filter(requestStatue=False)
    return render(request, 'request/request_detail.html', {'request':request_list})

def showFinishedRequests(request):
    request_list = Request.objects.filter(requestStatue=True)
    return render(request, 'request/request_detail.html', {'request':request_list})
