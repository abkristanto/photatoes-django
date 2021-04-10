from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
def index(request):

    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.info(request, 'Your message has been sent. Thank you!')
        return redirect("/")
        # return HttpResponse("<h1>THANKS FOR CONTACTING US</h1>")


    ports = Portfolio.objects.all()
    photographers = Photographer.objects.all()
    

    return render(request, "index.html", {'ports': ports, 'photographers': photographers})

def dynamic_lookup_view(request, my_id):
    obj = Portfolio.objects.get(id=my_id)
    context = {
        "port": obj
    }
    return render(request, "portfolio-details.html", context)

def photographers(request):
    photographers = Photographer.objects.all()
    return render(request, "photographers.html", {'photographers': photographers})