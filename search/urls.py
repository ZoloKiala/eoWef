
from django.urls import path
from . import views
from .views import contactView


urlpatterns = [
    path('home', views.index, name= 'index'),
    path('', views.search, name= 'search'),
    path('get_started/', views.get_started, name= 'get_started'),
    path('credits/', views.credits, name= 'credits'),
    path('contact/', contactView, name= 'contact'),
]
