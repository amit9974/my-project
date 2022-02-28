from email import message
from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def Index(request):
    return render(request, 'app/index.html')

def ContactUs(request):
    if request.method == "POST":
        name = request.POST['Name']
        email = request.POST['Email']
        subject = request.POST['Subject']
        message = request.POST['Message']

        user = ContactFrom.objects.create(name=name,email=email,subject=subject,message=message)
        user.save()
        return redirect('index')