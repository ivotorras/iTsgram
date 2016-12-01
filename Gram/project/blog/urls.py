
from django.conf.urls import url, include
from django.contrib import admin
from login.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^home/$', home, name='home'),
    url(r'^comentar/(\d+)$', comentar, name='comentar'),
=======
    url(r'^home/$', subir , name="subir" ),
    url(r'^home/$', home),
    url(r'^home/(?P<username>[-\w]+)$', perfilajeno),
    url(r'^home/(?P<username>[-\w]+)/fav$', favs),
>>>>>>> 937d2bf0a42ad63bc4d5e936e42dc338f6a30697
    url(r'^register/$', register , name="register"),
    url(r'^register/success/$', register_success),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
	url(r'^home/perfil/$', perfil , name="perfil"),
    url(r'^myapp/list/$', RedirectView.as_view(url='/login/', permanent=True)),
    url(r'^$', RedirectView.as_view(url='/login/', permanent=True)),
    url(r'^home/search/', 'login.views.search'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

