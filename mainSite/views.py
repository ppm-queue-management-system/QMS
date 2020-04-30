from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'mainSite/login.html')

def administrator(request):
    return render(request, 'mainSite/administrator.html')
