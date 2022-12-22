import requests
from django.conf import settings
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
User = settings.AUTH_USER_MODEL


class ObjectViewed(models.Model):
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)  # User instance
    # ip_address = models.CharField(max_length=220, blank=True, null=True) # IP Address
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE)  # Product, Post, User, Image
    # Product id, Post id, User id, Image id
    object_id = models.PositiveIntegerField()
    # Product instance, Post instance, User instance, Image instance
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)  # timestamp

    def __str__(self):
        return "%s viewed on %s" % (self.content_object, self.timestamp)

    class Meta:
        ordering = ['-timestamp']  # most recent saved show up first
        verbose_name = 'Object Viewed'
        verbose_name_plural = 'Objects Viewed'


class Translation(models.Model):
    source_language = models.CharField(max_length=2)
    target_language = models.CharField(max_length=2)
    source_text = models.TextField()
    translated_text = models.TextField(blank=True)

    def translate(self):
        # Set the API endpoint and API key
        endpoint = 'https://api-platform.systran.net/translation/text/translate'
        api_key = 'YOUR_API_KEY'

        # Set the payload for the API request
        payload = {
            'source': self.source_language,
            'target': self.target_language,
            'input': self.source_text
        }

        # Set the headers for the API request
        headers = {
            'X-Request-ID': 'unique_request_id',
            'X-Relayer-Host': 'api-platform.systran.net',
            'Authorization': f'Apikey {api_key}',
            'Content-Type': 'application/json'
        }

        # Make the API request
        response = requests.post(endpoint, json=payload, headers=headers)

        # Get the translated text from the response
        translated_text = response.json()['outputs'][0]['output']

        # Save the translated text to the model
        self.translated_text = translated_text
        self.save()

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         indexes = [
#             models.Index(fields=['name']),
#             models.Index(fields=['price']),
#         ]
