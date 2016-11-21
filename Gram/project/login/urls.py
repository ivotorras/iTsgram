from django.conf.urls import patterns, url, include
from registration import views
from login.views import *
from barra.models import *



urlpatterns = patterns('',
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),   
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^register/success/$',views.RegisterSuccessView.as_view(), name='register-success'),
    url(r'^$', 'barra.views.search'),                   
)
