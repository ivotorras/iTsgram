
from django.conf.urls import url, include
from django.contrib import admin
from login.views import *
from login.views import subir
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', subir , name="subir" ),
    url(r'^home/$', home),
    url(r'^register/$', register , name="register"),
    url(r'^register/success/$', register_success),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
	url(r'^home/perfil/$', perfil , name="perfil"),
    url(r'^myapp/list/$', RedirectView.as_view(url='/login/', permanent=True)),
    url(r'^$', RedirectView.as_view(url='/login/', permanent=True)),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

