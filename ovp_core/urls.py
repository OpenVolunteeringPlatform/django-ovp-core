from django.conf.urls import url, include

from ovp_core import views

urlpatterns = [
  url('^startup/', views.startup, name='startup'),
]
