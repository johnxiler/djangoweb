from django.contrib import admin

# Register your models here.
from .models import ObjectViewed, Translation, basicinfo

admin.site.register(ObjectViewed)
admin.site.register(Translation)
admin.site.register(basicinfo)
