from django.conf.urls import url

from library import views


urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^media/$', views.MediaListView.as_view(), name='media'),
	url(r'^media/(?P<pk>\d+)$', views.MediaDetailView.as_view(), name='media-detail'),
	#url(r'^search', views.search, name="Search"),
]