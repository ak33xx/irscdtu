from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from . import models

# Create your views here.
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
                        None,
                        p.email_id
                    )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(reverse('mailform'))
    return render(request, 'mail_form.html', {'form': form})
