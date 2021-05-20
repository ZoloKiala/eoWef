
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('search_data/', views.search_data, name= 'search_data'),
    path('get_started/', views.get_started, name= 'get_started'),
    path('credits/', views.credits, name= 'credits'),
    path('contact/', views.contact, name= 'contact'),
]
