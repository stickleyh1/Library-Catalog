from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
import datetime as dt

from django.db.models import Q
from django.contrib.auth.models import User
from library.models import Media, MediaInstance, Genre

def index(request):
	context_dict={}
	context_dict['num_media'] = Media.objects.all().count()
	context_dict['num_inst'] = MediaInstance.objects.all().count()
	context_dict['num_avail'] = MediaInstance.objects.filter(status__exact='a').count()
	return render(request, 'library/index.html', context_dict)

def search(request):
	if request.GET.get('q'):
		query = ''+request.GET.get('q')
		if query != None:
			return render(request, 'library/search_results.html')
		
	return render(request, 'library/search.html')

def search_results(request):
	if request.GET.get('q'):
		query = ''+request.GET.get('q')
		if query != None:
			print("Not None")
			results = []
			count = 0
			objs = Media.objects.filter(Q(isbn=query) | Q(topic__name=query) | Q(title__icontains=query))
			print(objs)
			for m in objs:
				print(count)
				count += 1
				results.append(m)
			return render(request, 'library/search_results.html', {"results": results,})
		
	return render(request, 'library/search.html')

class MediaListView(generic.ListView):
    model = Media

class MediaDetailView(generic.DetailView):
    model = Media

class UserListView(generic.ListView):
    model = User

class UserDetailView(generic.DetailView):
	model = User

	def get_context_data(self, **kwargs):
		context = super(UserDetailView, self).get_context_data(**kwargs)
		context['instances'] = MediaInstance.objects.all()
		context['medias'] = Media.objects.all()
		for i in context['instances']:
			if i.due_date < dt.date.today():
				i.late_fee = (dt.date.today() - i.due_date).days

		return context