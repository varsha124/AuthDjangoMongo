from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def method1(request):
    return render(request,"health/startpage.html")
    return HttpResponse("HEllo World")
    