from django.shortcuts import render
from .forms import UserForm,ProfileForm

# Create your views here.

def home(request):
    context={}
    context['user']=UserForm
    context['profile']=ProfileForm

    return render (request,'home.html',context)

def userdata(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
