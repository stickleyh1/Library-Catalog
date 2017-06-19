from django.conf.urls import url

from library import views


urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^media/$', views.MediaListView.as_view(), name='media'),
	url(r'^media/(?P<pk>\d+)$', views.MediaDetailView.as_view(), name='media-detail'),
	url(r'^user/$', views.UserListView.as_view(), name="user"),
	url(r'^user/(?P<pk>\d+)/$', views.UserDetailView.as_view(), name="user-detail"),
	url(r'^search/$', views.search, name="search"),
	url(r'^search_results/$', views.search_results, name="search_results"),
]