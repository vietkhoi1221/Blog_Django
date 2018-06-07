from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request,'pages/home.html')
def contact(request):
    return render(request,'pages/contact.html')
def error(request):
    return render(request,'pages/error.html')
def register(request):
    form = RegistrationForm()
    if request.method == "POST": #chung to nguoi dung da nhap
        form = RegistrationForm(request.POST)
        if form.is_valid(): #neu bang tru thi tat ca cac ham ben forms.py deu hop le
            form.save()
            return HttpResponseRedirect("/")
    return render(request,'pages/register.html',{"form":form})    

