from django import forms
from mainSite.models import SigninModel, BookTicketModel, AdjustTicketModel, CancelTicketModel

class SigninForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'sign'}), label='Username')
    password = forms.CharField(widget=forms.TextInput(attrs={'class' : 'sign'}), label='Password')
    
    class Meta:
        model = SigninModel
        fields = ('username', 'password',)

class BookTicketForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(attrs={'class' : 'sign'}), label='')
    
    class Meta:
        model = BookTicketModel
        fields = ('post',)

class AdjustTicketForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(attrs={'class' : 'sign'}), label='')
    
    class Meta:
        model = AdjustTicketModel
        fields = ('post',)
    
class CancelTicketForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(attrs={'class' : 'sign'}), label='')
    
    class Meta:
        model = CancelTicketModel
        fields = ('post',)
        

    