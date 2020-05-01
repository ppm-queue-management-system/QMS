from django import forms

class AdjustTicketForm(forms.Form):
    post = forms.CharField(widget=forms.TextInput(attrs={'class' : 'sign'}), label='')
    
class CancelTicketForm(forms.Form):
    post = forms.CharField(widget=forms.TextInput(attrs={'class' : 'sign'}), label='')

class BookTicketForm(forms.Form):
    post = forms.CharField(widget=forms.TextInput(attrs={'class' : 'sign'}), label='')
    