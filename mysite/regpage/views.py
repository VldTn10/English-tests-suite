from django.shortcuts import render

# Create your views here.
def regPage_list(request):
	return render(request, 'regpage/regPage_list.html', {})