from django.urls import path

from . import views

app_name = 'sessions'
urlpatterns = [
    path('', views.SessionIndexView.as_view(), name='session_index'),
    path('<int:pk>/', views.SessionDetailView.as_view(), name='detail'),
    path('tunelist/', views.TuneListView.as_view(), name="tune_list"),
    path('newsession/', views.NewSessionView.as_view(), name='new_session')
]