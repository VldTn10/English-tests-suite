from django.shortcuts import render
from .models import regPage
from django.utils import timezone

# Create your views here.
def regPage_list(request):
	logins = regPage.objects
	account = regPage.objects.filter(creating_date__lte = timezone.now()).order_by('creating_date')
	return render(request, 'regpage/regPage_list.html', {'accounts': account})