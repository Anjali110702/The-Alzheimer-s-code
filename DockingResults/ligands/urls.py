from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('home/results/', views.results, name='results'),
    path('about/', views.about, name='about'),
    path('home/results/sim/', views.simulations, name='simulations'),
]
