from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from library.models import Media, UserProfile, MediaInstance, Genre

def index(request):
	context_dict={}
	context_dict['num_media'] = Media.objects.all().count()
	context_dict['num_inst'] = MediaInstance.objects.all().count()
	context_dict['num_avail'] = MediaInstance.objects.filter(status__exact='a').count()
	return render(request, 'library/index.html', context_dict)

class MediaListView(generic.ListView):
    model = Media

class MediaDetailView(generic.DetailView):
    model = Media