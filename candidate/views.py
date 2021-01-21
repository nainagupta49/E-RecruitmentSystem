from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .forms import RegisterForm

def login(request,*args, **kwargs):
    return render(request,"pages/login.html",context={},status=200)


def signup(request,*args, **kwargs):
    if request.method == 'POST':
        name1 = request.POST.get('UserName')
        print(name1)
    return render(request,"pages/signup.html",context={},status=200)

def register(request,*args, **kwargs):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        form = RegisterForm()
    context = {
        'form':form
    }
    return render(request,"pages/register.html",context,status=200)