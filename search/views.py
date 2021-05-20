from django.shortcuts import render
from .models import SatModel, Variables

# Create your views here.
def index(request):
    return render(request, 'search/index.html')

def search_data(request):
    all_satmodel = SatModel.objects.all()
    return render(request, 'search/search_data.html', {'all_satmodel': all_satmodel})

def get_started(request):
    return render(request, 'search/get_started.html')

def credits(request):
    return render(request, 'search/credits.html')

def contact(request):
    return render(request, 'search/contact.html')
