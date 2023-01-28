from django.urls import path
from . import views

# URLConfigurations

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('features', views.features, name='features'),
    path('contact', views.contact, name='contact'),
    path('crudgen', views.crudgen, name='crudgen'),
]
