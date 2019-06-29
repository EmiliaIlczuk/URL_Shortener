from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='Shortener'),
    path('makeshort/', views.shorten_url, name='Shorten'),
    path('<slug:short_code>/', views.redirect_original, name='Scode'),

]