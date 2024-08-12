from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse

# Create your views here.

def django_register(request):
    ERFO = RegisterDjangoModel()
    d = {'ERFO': ERFO}
    if request.method == 'POST':
        RFDO = RegisterDjangoModel(request.POST)
        if RFDO.is_valid():
            name = RFDO.cleaned_data['name']
            pno = RFDO.cleaned_data['pno']
            email = RFDO.cleaned_data['email']
            add = RFDO.cleaned_data['add']
            un = RFDO.cleaned_data['username']
            pw = RFDO.cleaned_data['password']
            reg = Register(name = name, pno=pno, email=email, add=add, username=un
                           , password=pw)
            reg.save()
            return HttpResponse('Done')
        return HttpResponse('Invalid Data')
    return render(request, 'django_register.html', d)


def model_register(request):
    ERFO = RegisterModelForm()
    d = {'ERFO': ERFO}
    if request.method == 'POST':
        RFDO = RegisterModelForm(request.POST)
        if RFDO.is_valid():
            RFDO.save()
            return HttpResponse('Done....')
        return HttpResponse('Invalid Data')
    return render(request, 'model_register.html', d)