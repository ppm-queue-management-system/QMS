from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.template import RequestContext
from mainSite.forms import  SigninForm, AdjustTicketForm, CancelTicketForm, BookTicketForm

# Create your views here.
class SigninView(TemplateView):
    template_name = 'mainSite/login.html'
    
    def get(self, request):
        form = SigninForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.save(commit=False)
            password = form.save(commit=False)
            username.save()
            password.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            form = SigninForm()
            if 'N' in username or 'n' in username:
                return redirect('../student')
            else:
                return redirect('../operator')
        args = {'form':form, 'username':username, 'password':password}
        return render(request, self.template_name, args)

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
            post = form.save(commit=False)
            post.save()
            time = form.cleaned_data['post']
            form = BookTicketForm()
            return redirect('../student')
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
            post = form.save(commit=False)
            post.save()
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
            post = form.save(commit=False)
            post.save()
            time = form.cleaned_data['post']
            form = CancelTicketForm()
            return redirect('../student')
        args = {'form':form, 'time':time}
        return render(request, self.template_name, args)