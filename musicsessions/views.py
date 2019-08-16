from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Session, Tune

# Create your views here.
class SessionIndexView(generic.ListView):
    template_name = 'musicsessions/session_index.html'
    context_object_name = 'session_list'

    def get_queryset(self):
        return Session.objects.all().order_by('-start_date')

class SessionDetailView(generic.DetailView):
    model = Session
    template_name = 'musicsessions/session_detail.html'

    def get_queryset(self):
        """
        Filters to get the sessions we want other people to be able to view
        the details of.
        """
        # Must change when adding Active to session properties.
        return Session.objects.all()

class TuneListView(generic.ListView):
    template_name = 'musicsessions/tune_list.html'
    context_object_name = 'tune_list'

    def get_queryset(self):
        return Tune.objects.all().order_by('name')

class AddTuneToSessionView(generic.ListView):
    template_name = ''
    context_object_name = 'tune_list'

    def get_queryset(self):
        return Tune.objects.all().order_by('name')

def index(request):
    return HttpResponse("This is the session index.")

def add_tune_to_session(request):
    pass