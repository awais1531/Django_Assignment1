from django.shortcuts import render

# Create your views here.

def detail(request):
    return render(request,"myapp/detail.html")

def index(request):
    return render(request,"myapp/index.html")
    
