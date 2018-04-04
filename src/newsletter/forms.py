from django import forms

class MailForm(forms.Form):
    subject = forms.CharField(widget=forms.Textarea)
    message = forms.CharField(widget=forms.Textarea)
