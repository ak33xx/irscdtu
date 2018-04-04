from django.shortcuts import render
from . import models

def send_report(request):
    if request.method == 'POST':
        rep = models.Report()
        rep.name = request.POST.get("name")
        rep.email = request.POST.get("email")
        rep.message = request.POST.get("message")
        rep.save()
    return render(request, "index.html")
