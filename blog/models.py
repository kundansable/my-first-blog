from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from custom_user.models import AuthUser

class Post(models.Model):
    author = models.ForeignKey('custom_user.AuthUser')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class login(models.Model):
	
	username = models.CharField(max_length=200)	
	password = models.CharField(max_length=200)

	def __str__(self):
		return self.username

