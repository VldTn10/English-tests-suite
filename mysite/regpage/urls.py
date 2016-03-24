from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.regPage_list, name='regPage_list'),
]