from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, url
from django.conf.urls import include
from django.contrib import admin
from django.views.generic import RedirectView
urlpatterns = [
	url(r'^$', RedirectView.as_view(url='/library/', permanent=True)),
    url(r'^admin/', admin.site.urls),
    url(r'^library/', include('library.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)