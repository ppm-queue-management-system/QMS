from django.views.generic import TemplateView
from django.shortcuts import render

from django.template import RequestContext

from mainSite.forms import  HomeForm

# Create your views here.
def login(request):
    return render(request, 'mainSite/login.html')

def student(request):
    return render(request, 'mainSite/student.html')

def adjustTicket(request):
    return render(request, 'mainSite/adjustTicket.html')

def cancelTicket(request):
    return render(request, 'mainSite/cancelTicket.html')

def index(request):
    return render(request, 'mainSite/index.html')

class HomeView(TemplateView):
    template_name = 'mainSite/bookTicket.html'
    
    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = HomeForm()
        args = {'form':form, 'text':text}
        return render(request, self.template_name, args)