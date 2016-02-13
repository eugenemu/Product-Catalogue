from django.conf.urls import patterns, url
from apps.products import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add/', views.add, name='add'),
	url(r'^back/', views.back, name='back'),
	url(r'^show/(?P<product_id>\d+)/', views.show, name='show'),
	url(r'^remove/(?P<product_id>\d+)/', views.remove, name='remove'),
	url(r'^update/(?P<product_id>\d+)/', views.update, name='update'),
]