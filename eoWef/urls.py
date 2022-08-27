
from django.contrib import admin
from django.urls import path, include
from search import views
from rest_framework import routers


router = routers.SimpleRouter()

router.register(r'variables', views.VariableModelViewSet, basename = 'variable')
router.register(r'satmodels', views.SatModelModelViewSet, basename = 'satmodel')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('units/', views.UnitListAPIView.as_view(), name="units"),
    path('sectors/', views.SectorListAPIView.as_view(), name="sectors"),
    path('', include('search.urls'))

] + router.urls
