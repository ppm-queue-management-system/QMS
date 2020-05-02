from django import forms
from mainSite.models import BookTicketModel, AdjustTicketModel, CancelTicketModel

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


    