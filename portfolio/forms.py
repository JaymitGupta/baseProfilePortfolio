from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}),required=True)
    response = forms.CharField(widget=forms.Textarea(attrs={'class' : 'form-control'}),required=True)
