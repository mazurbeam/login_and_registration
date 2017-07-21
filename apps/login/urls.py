from django.conf.urls import url
from . import views

def test(request):
    print request.POST

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
]
