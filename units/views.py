from django.shortcuts import render
from .models import Part, Unit

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
