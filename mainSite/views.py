from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.template import RequestContext
from mainSite.forms import  AdjustTicketForm, CancelTicketForm, BookTicketForm

# Create your views here.
def login(request):
    return render(request, 'mainSite/login.html')

def administrator(request):
    return render(request, 'mainSite/administrator.html')

def operator(request):
    return render(request, 'mainSite/operator.html')

def student(request):
    return render(request, 'mainSite/student.html')

class BookTicketView(TemplateView):
    template_name = 'mainSite/bookTicket.html'
    
    def get(self, request):
        form = BookTicketForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = BookTicketForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['post']
            form = BookTicketForm()
            return redirect('../bookTicket')
        args = {'form':form, 'time':time}
        return render(request, self.template_name, args)

class AdjustTicketView(TemplateView):
    template_name = 'mainSite/adjustTicket.html'
    
    def get(self, request):
        form = AdjustTicketForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = AdjustTicketForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['post']
            form = AdjustTicketForm()
            return redirect('../adjustTicket')
        args = {'form':form, 'time':time}
        return render(request, self.template_name, args)
    
class CancelTicketView(TemplateView):
    template_name = 'mainSite/cancelTicket.html'
    
    def get(self, request):
        form = CancelTicketForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = CancelTicketForm(request.POST)
        if form.is_valid():
            time = form.cleaned_data['post']
            form = CancelTicketForm()
            return redirect('../student')
        args = {'form':form, 'time':time}
        return render(request, self.template_name, args)