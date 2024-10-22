from django.shortcuts import render, HttpResponse
from datetime import datetime  # Make sure to import datetime
from home.models import Contact

def index(request):
    # context ={
    #   'variable1':"this is sent",
    #   'variable2':"Hi Aayushma"
    # }
    return render(request, 'index.html')
    # return HttpResponse("This is homepage...")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is about page...")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is services page...")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        if name and email and phone and desc:  
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()

        

    return render(request, 'contact.html') # Move return statement outside the if block
    # return HttpResponse("This is contact page...")
