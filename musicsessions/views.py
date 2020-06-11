from django.shortcuts import render
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

from .models import Session, Tune, SessionTune

import datetime

#=======================================================
# Forms
#=======================================================

class SessionCreateForm(ModelForm):
    # The form for creating a new session.
    class Meta:
        model = Session
        exclude = ('start_date','tunes')
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('start_date')
        super(SessionCreateForm, self).__init__(*args, **kwargs)

#=======================================================
# Views
#=======================================================

# Create your views here.
class SessionIndexView(generic.ListView):
    # The view for all created sessions.
    template_name = 'musicsessions/session_index.html'
    context_object_name = 'session_list'

    def get_queryset(self):
        return Session.objects.all().order_by('-start_date')

class SessionDetailView(generic.DetailView):
    # The view for showing details for a specific Jam Session.
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
    # The view for showing all available tunes within the software
    template_name = 'musicsessions/tune_list.html'
    context_object_name = 'tune_list'

    def get_queryset(self):
        return Tune.objects.all().order_by('name')

class AddTuneToSessionView(generic.UpdateView):
    # The view for adding a tune to an active session
    # TODO: Finish
    model = SessionTune
    fields = ['tune']
    template_name = 'musicsessions/sessiontune_update.html'
    context_object_name = 'tune_list'
    success_url = ''

    def get_queryset(self):
        return Tune.objects.all().order_by('name')

class NewSessionView(generic.CreateView):
    # The view for creating a new session
    form_class = SessionCreateForm
    template_name = 'musicsessions/session_form.html'
    success_url = 'sessions:session_index'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.start_date = datetime.datetime.now()
        self.object.save()
        return HttpResponseRedirect(reverse(self.get_success_url()))

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(NewSessionView, self).get_form_kwargs(*args, **kwargs)
        kwargs['start_date'] = datetime.datetime.now()
        return kwargs

#=======================================================
# Other Functions
#=======================================================

def makesession(request):
    pass

def index(request):
    return HttpResponse("This is the session index.")

def add_tune_to_session(request):
    pass