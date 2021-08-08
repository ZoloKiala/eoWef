from django.shortcuts import render
from .models import SatModel, Variables
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    return render(request, 'search/index.html')

def search(request):
    all_satmodel = SatModel.objects.all()
    return render(request, 'search/search.html', {'all_satmodel': all_satmodel})

def get_started(request):
    return render(request, 'search/get_started.html')

def credits(request):
    return render(request, 'search/credits.html')

def contactView(request):
    if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
            subject = "Eo-wef Inquiry" 
            name = form.cleaned_data['name']
            body = {
            'name': form.cleaned_data['name'], 
            'email': form.cleaned_data['from_email'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, os.environ.get('EMAIL'), [os.environ.get('EMAIL')]) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'search/contact.html', {'name':name})
      
    form = ContactForm()
    return render(request, "search/contact.html", {'form':form})


    # def contactView(request):
    #     if request.method == "POST":
    #     message_name =  request.POST['name']
    #     message_subject =  request.POST['subject']
    #     message_email =  request.POST['from_email']
    #     message =  request.POST['message']

    #     send_mail(
    #         message_subject, #subject
    #         message, # message
    #         message_email, #from email
    #         ['zolokiala@gmail.com'],
    #     )

    #     return render(request, 'search/contact.html', {'message_name':'message_name'})

    # form = ContactForm()
    # return render(request, 'search/contact.html', {'form':form})
