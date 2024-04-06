from django.shortcuts import render

# Create your views here.
def loging(request):
    return render(request,'loging.html')
def home(request):
    return render(request,'home.html')