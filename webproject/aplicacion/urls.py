from django.urls import path
from aplicacion import views

urlpatterns = [
    path('',views.index, name='index'),
    path('viernes/',views.viernes, name='viernes'),
    path('peliculas/',views.peliculas,name='peliculas')]