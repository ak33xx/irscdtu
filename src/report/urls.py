from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = "report"

urlpatterns = [
    url(r'^$', views.send_report, name='report'),
]

urlpatterns += staticfiles_urlpatterns()
