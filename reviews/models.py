from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your models here.
class Review(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	review = models.TextField()
	vote_ups = models.IntegerField(default=0)
	vote_downs = models.IntegerField(default=0)
	published_date = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(
		unique=True,
		default=get_random_string,
		max_length=13,
	)

	def __unicode__(self):
		return self.title

	def publish(self):
		published_date = timezone.now()
		published_date.save()
