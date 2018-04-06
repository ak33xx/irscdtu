from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import models

def send_report(request):
    if request.method == 'POST':
        rep = models.Report()
        rep.name = request.POST.get("name")
        rep.email = request.POST.get("email")
        rep.message = request.POST.get("message")
        rep.save()
    return HttpResponseRedirect(reverse('home'))
