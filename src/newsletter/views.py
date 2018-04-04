from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from . import models
from . import forms

# Create your views here.
@login_required
def send_email(request):
    form = forms.MailForm()
    if request.method == 'POST':
        form = forms.MailForm(request.POST)
        if form.is_valid():
            q = models.MailTo.objects.all()
            for p in q:
                try:
                    send_mail(
                        form.cleaned_data['subject'],
                        form.cleaned_data['message'],
                        "gulasnani7@gmail.com",
                        [p.email_id]
                    )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(reverse('mailform'))
    return render(request, 'newsletter/mail_form.html', {'form': form})
