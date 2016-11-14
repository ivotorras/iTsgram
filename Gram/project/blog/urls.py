
from django.conf.urls import url, include
from django.contrib import admin
from login.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', home),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^myapp/list/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^perfil/$','django.contrib.auth.perfil'),
	url(r'^home/perfil/$', perfil , name="perfil"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

