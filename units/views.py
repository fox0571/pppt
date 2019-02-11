from django.shortcuts import render
from .models import Part, Unit
from request.models import PartRequest
from django.http import JsonResponse

def check_part(request):
	if request.method == "POST":
		model=request.POST.get("model","")
		part=request.POST.get("part","")
		if model:
			units=Part.objects.filter(unit__model__icontains=model)
			return render(request, 'part/check.html', {'request':units})
		if part:
			parts=Unit.objects.filter(parts__number__icontains=part)
			return render(request, 'part/check.html', {'request':parts})
	return render(request, 'part/check.html')

def get_total(e):
	return e['total']

def get_top_20_req(request):
	p_list=[]
	for p in Part.objects.all():
		dic={}
		dic['number']=p.number
		dic['discription']=p.name_eng
		dic['total']=p.partrequest_set.all().count()
		p_list.append(dic)
	p_list.sort(reverse=True,key=get_total)
	return JsonResponse(p_list[:20],safe=False)
def part_stat(request):
	parts=Part.objects.all()
	if request.method == "GET":
		part_number = request.GET.get("number","")
		try:
			part = parts.get(number=part_number)

			request_set=part.partrequest_set.all()
			data={}
			for r in request_set:
				date = r.request_time.isoformat()
				qty = r.qty
				if date in data:
					data[date]=data[date]+qty
				else:
					data[date]=qty
		except Part.DoesNotExist:
			data={"ERROR":"NO SUCH A PART NUMBER"}
		return JsonResponse(data)



		