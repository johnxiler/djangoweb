from django.urls import path
from . import views

# URLConfigurations

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.about, name='about'),
    path('', views.features, name='features'),
    path('', views.contact, name='contact'),
]
