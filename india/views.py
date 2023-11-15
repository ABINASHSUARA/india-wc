from django.shortcuts import render
from django.http import HttpResponse

def virat(request):
    return render(request,'virat.html')

def iyer(request):
    return HttpResponse("best  batsman")

# Create your views here.
