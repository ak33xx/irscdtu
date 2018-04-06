from django import forms

class MailForm(forms.Form):
    subject = forms.CharField(widget=forms.Textarea(attrs={
                                    'rows':3,
                                    'cols':100
                                }))
    message = forms.CharField(widget=forms.Textarea(attrs={
                                    'rows':8,
                                    'cols':100
                                }))
