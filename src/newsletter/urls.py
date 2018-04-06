from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = "newsletter"

urlpatterns = [
    url(r'^$', views.send_email, name='send_email'),
    url(r'^visitor/$', views.save_visitor, name='visitor'),
]

urlpatterns += staticfiles_urlpatterns()
