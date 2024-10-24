from django.shortcuts import render
from .forms import UserForm,ProfileForm

# Create your views here.

def home(request):
    context={}
    context['user']=UserForm
    context['profile']=ProfileForm

    return render (request,'home.html',context)
