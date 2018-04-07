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
                        'Hi {} !\n\n'.format(p.name) + form.cleaned_data['message'],
                        "solvedtu@gmail.com",
                        [p.email_id]
                    )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(reverse('newsletter:send_email'))
    return render(request, 'newsletter/mail_form.html', {'form': form})

def save_visitor(request):
    if(request.method == 'POST'):
        person = models.MailTo()
        person.name = request.POST.get("name")
        person.email_id = request.POST.get("email")
        person.save()
        try:
            send_mail(
                "IRSC DTU | Signup for newsletter",
                'Hi {} !\n\n'.format(person.name) + "Thank you for signing up for our newsletter. We promise you regular updates on road safety, be them new or prevalent laws on the same, or be them awareness programs in your neighbourhood. We'll be glad to also share with you our own initiatives and campaigns, and how you can be a part of something so crucial to the society.\n\nRegards,\nIRSC DTU",
                "solvedtu@gmail.com",
                [person.email_id]
            )
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
    return render(request, "index.html")
