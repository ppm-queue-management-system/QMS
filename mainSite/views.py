from django.shortcuts import render

from django.template import RequestContext

# Create your views here.
def login(request):
    return render(request, 'mainSite/login.html')

def student(request):
    return render(request, 'mainSite/student.html')

def adjustTicket(request):
    return render(request, 'mainSite/adjustTicket.html')

def cancelTicket(request):
    return render(request, 'mainSite/cancelTicket.html')

def bookTicket(request):
    return render(request, 'mainSite/bookTicket.html')

def index(request):
    return render(request, 'mainSite/index.html')

def timeSlot(request):
    return render(request, 'mainSite/timeSlot.php')