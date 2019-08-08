from django.urls import path

from . import views

app_name = 'sessions'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.SessionDetailView.as_view(), name='detail'),
]