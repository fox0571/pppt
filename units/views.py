from django.shortcuts import render
from .models import Part, Unit

def check_part(request):
	if request.method == "POST":
		model=request.POST.get("model","")
		all=Part.objects.filter(unit__model=model)
		return render(request, 'part/check.html', {'request':all})
	return render(request, 'part/check.html')
