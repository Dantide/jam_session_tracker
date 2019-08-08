from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Session, Tune

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'musicsessions/index.html'
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
    model = Tune
    template_name = ""

    def get_queryset(self):
        return Tune.objects.all().order_by('name')

def index(request):
    return HttpResponse("This is the session index.")