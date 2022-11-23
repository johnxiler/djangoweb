from django.urls import path
from . import views

# URLConfigurations

urlpatterns = [
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('features', views.features, name='features'),
    path('contact', views.contact, name='contact'),
]
