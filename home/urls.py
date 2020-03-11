from django.urls import path

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cs', views.homeCS, name='home-cs'),
    path('music', views.homeMusic, name='music')
]
