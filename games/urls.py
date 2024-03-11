from django.urls import path, re_path as url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.HomePageView.as_view(), name='home'),
    path('questions/', views.QuestionPageView.as_view(), name='questions'),
    path('resultsfilter/', views.FilterView.as_view(), kwargs=None, name='resultsfilter'),

]