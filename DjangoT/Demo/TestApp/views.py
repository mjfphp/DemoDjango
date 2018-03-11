from django.shortcuts import render
from django.http import HttpResponse
from TestApp import models
from TestApp import forms
from TestApp.des import Crypter

# Create your views here.
def Index(request):
    return HttpResponse('Welcome to page index')
def Home(request):
    data = {
        'name': 'Mohamed', 'age': 18, 'country': 'Morocoo',
         'loisirs':['sport','chess','food']
            }
    return render(request, 'index.html', data)
def Sd(request,sid):
    return HttpResponse('your id is :'+sid)
def Students(request):
    d=models.Student.objects.all()
    data={'s':d}
    return render(request,'students.html',data)

def Register(request):
    msg=''
    form_data=forms.UserRegistrar(request.POST or None)
    if form_data.is_valid():
        s=models.Student()
        s.fname=form_data.cleaned_data['fname']
        s.lname=form_data.cleaned_data['lname']
        s.age=form_data.cleaned_data['age']
        s.dn=form_data.cleaned_data['dn']
        s.save()
        msg='Data is valid'
    data={'Form':form_data,'msg':msg}
    return render(request,'register.html',data,msg)
def Crypt(request):
    form_data=forms.CryptMsg(request.POST or None)
    msg=''
    if form_data.is_valid():
      Msg=form_data.cleaned_data['Msg']
      Cle=form_data.cleaned_data['Cle']
      r=Crypter(Msg,Cle)
      msg="%r"%r
    data = {'Form': form_data,'msg': msg}
    return render(request,'des.html',data,msg)


