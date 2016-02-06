from __future__ import unicode_literals
import os
import uuid
from django.db import models

from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import User
from registration.signals import user_registered
from django.conf import settings
from django.utils.crypto import get_random_string
from autoslug import AutoSlugField
from PIL import Image
from django.core.validators import MaxValueValidator

class Book(models.Model):
	Genres = (
	('Non-Fiction', (
		('Biography','Biography'),
		('Business','Business'),
		('Computer','Computer'),
		('Fiction','Fiction'),
		('Finance', 'Finance'),
		('Food & Beverages','Food & Beverages'),
		('Graphic novels/Manga','Graphic novels/Manga'),
		('History','History'),
		('Law','Law'),
		('Medical','Medical'),
		('Religion','Religion'),
		('Sports','Sports'),
		('Technology & Engineering','Technology & Engineering'),
		)
	),
	('Fiction', (
			('Adventure', 'Adventure'),
			('Classics', 'Classics'),
			('Contemporary Fiction', 'Contemporary Fiction'),
			('Crime', 'Crime'),
			('Fantasy', 'Fantasy'),
			('Horror', 'Horror'),
			('Romance', 'Romance'),
			('Science Fiction', 'Science Fiction'),
			('Thrillers', 'Thrillers'),
		)
	),
	('School Textbooks', (
			('math','math'),
			
		)
	),
)
	user = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	genre = models.CharField(max_length=100,choices=Genres)
	description = models.TextField()
	personal_review = models.TextField(blank=True)
	price = models.IntegerField(validators=[MaxValueValidator(99999)])
	published_date = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(
		unique=True,
		default=get_random_string,
		max_length=13,
	)
	sold = models.BooleanField(default=False)
	# genslug = AutoSlugField(populate_from='genre',null=True, blank=True)
	def publish(self):
		published_date = timezone.now()
		published_date.save()

	def __unicode__(self):
		return self.title

# def upload_location(instance, filename):
# 	return "%s/%s" %(instance.id, filename)
class UserProfile(models.Model):
	user =  models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
	image = models.ImageField(
            null=True,
            blank=True)
	slug = AutoSlugField(populate_from='user',null=True, blank=True)
	shelf = models.ManyToManyField(Book, blank=True)
	address = models.CharField(max_length=999)
	contact_number = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(99999999)])
#to activate shell, do {{ object.shelf.all }} in templates.

	
	def __unicode__(self):
		return self.user.username
# this is required when you override save functions

class Rating(models.Model):
	user =  models.ForeignKey(User, related_name='user')
	author = models.ForeignKey(User, related_name='author',blank=True)
	Levels =(
		('Good','Good'),
		('Neutral','Neutral'),
		('Bad','Bad'),
		)
	rate = models.CharField(max_length=100, choices=Levels,null=True, blank=True)
	feedback = models.TextField(null=True, blank=True)
	published_date = models.DateField(default=timezone.now)


# @receiver(models.signals.post_delete, sender=UserProfile)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
# 	"""Deletes file from filesystem
# 	when corresponding `UserProfile` object is deleted.
# 	"""
# 	if instance.image:
# 		if os.path.isfile(instance.image.path):
# 			os.remove(instance.image.path)

# @receiver(models.signals.pre_save, sender=UserProfile)
# def auto_delete_file_on_change(sender, instance, **kwargs):
# 	"""Deletes file from filesystem
# 	when corresponding `UserProfile` object is changed.
# 	"""
# 	if not instance.pk:
# 		return False

# 	try:
# 		old_file = UserProfile.objects.get(pk=instance.pk).image
# 	except UserProfile.DoesNotExist:
# 		return False

# 	new_file = instance.image
# 	if not old_file == new_file:
# 		if os.path.isfile(old_file.path):
# 			os.remove(old_file.path)

def assure_user_profile_exists(username):
	"""
	Creates a user profile if a User exists, but the
	profile does not exist.  Use this in views or other
	places where you don't have the user object but have the pk.
	"""
	user = User.objects.get(pk=username)
	try:
		# fails if it doesn't exist
		userprofile = user.userprofile
	except UserProfile.DoesNotExist, e:
		userprofile = UserProfile(user=user)
		userprofile.save()
	return
def create_user_profile(**kwargs):
	UserProfile.objects.get_or_create(user=kwargs['user'])


user_registered.connect(create_user_profile)