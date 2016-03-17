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
from PIL import Image, ExifTags
from django.core.validators import MaxValueValidator
import django_filters
from types import MethodType
class Book(models.Model):
	Genres = (
	('Non-Fiction', (
		('Biography','Biography'),
		('Business','Business'),
		('Computer','Computer'),
		('Engineering', 'Engineering'),
		('Finance', 'Finance'),
		('Food','Food & Beverages'),
		('History','History'),
		('Law','Law'),
		('Manga', 'Manga'),
		('Medical','Medical'),
		('Novel', 'Novel'),
		('Religion','Religion'),
		('Sports','Sports'),
		('Technology','Technology'),
		)
	),
	('Fiction', (
		('Action', 'Action'),
		('Adventure', 'Adventure'),
		('Classics', 'Classics'),
		('Crime', 'Crime'),
		('Fantasy', 'Fantasy'),
		('Horror', 'Horror'),
		('Romance', 'Romance'),
		('ScienceFiction', 'Science Fiction'),
		('Thrillers', 'Thrillers'),
		)
	),
	('School Books', (
		('Secondary','Secondary'),
		('Primary','Primary'),
		('Polytechnic','Polytechnic'),
		('juniorcollege','Junior College'),
		('university', 'University'),
			
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
	image1 = models.ImageField(
            null=True,
            blank=True)
	image2 = models.ImageField(
            null=True,
            blank=True)
	image3 = models.ImageField(
            null=True,
            blank=True)
	image4 = models.ImageField(
            null=True,
            blank=True)
	# genslug = AutoSlugField(populate_from='genre',null=True, blank=True)
	def publish(self):
		published_date = timezone.now()
		published_date.save()

	def __unicode__(self):
			return self.title

	def save(self, *args, **kwargs):
		# this is required when you override save functions
		super(Book, self).save(*args, **kwargs)
	# our new code

		if self.image1:
				
			image1 = Image.open(self.image1)
			i_width, i_height = image1.size
			max_size = (1000,750)
			try:
			    for orientation in ExifTags.TAGS.keys():
			        if ExifTags.TAGS[orientation]=='Orientation':
			            break
			    exif=dict(image1._getexif().items())

			    if exif[orientation] == 3:
			        image1=image1.rotate(180, expand=True)
			    elif exif[orientation] == 6:
			        image1=image1.rotate(270, expand=True)
			    elif exif[orientation] == 8:
			        image1=image1.rotate(90, expand=True)
			    image1.save(self.image1.path)

			except (AttributeError, KeyError, IndexError):
			    # cases: image don't have getexif
			    pass
			image1.thumbnail(max_size, Image.ANTIALIAS)
			image1.save(self.image1.path)
		if self.image2:
				
			image2 = Image.open(self.image2)
			i_width, i_height = image2.size
			max_size = (1000,750)
			try:
			    for orientation in ExifTags.TAGS.keys():
			        if ExifTags.TAGS[orientation]=='Orientation':
			            break
			    exif=dict(image2._getexif().items())

			    if exif[orientation] == 3:
			        image=image.rotate(180, expand=True)
			    elif exif[orientation] == 6:
			        image2=image2.rotate(270, expand=True)
			    elif exif[orientation] == 8:
			        image2=image2.rotate(90, expand=True)
			    image2.save(self.image2.path)

			except (AttributeError, KeyError, IndexError):
			    # cases: image don't have getexif
			    pass
			image2.thumbnail(max_size, Image.ANTIALIAS)
			image2.save(self.image2.path)
		if self.image3:
				
			image3 = Image.open(self.image3)
			i_width, i_height = image3.size
			max_size = (1000,750)
			try:
			    for orientation in ExifTags.TAGS.keys():
			        if ExifTags.TAGS[orientation]=='Orientation':
			            break
			    exif=dict(image3._getexif().items())

			    if exif[orientation] == 3:
			        image3=image3.rotate(180, expand=True)
			    elif exif[orientation] == 6:
			        image3=image3.rotate(270, expand=True)
			    elif exif[orientation] == 8:
			        image3=image3.rotate(90, expand=True)
			    image3.save(self.image3.path)

			except (AttributeError, KeyError, IndexError):
			    # cases: image don't have getexif
			    pass
			image3.thumbnail(max_size, Image.ANTIALIAS)
			image3.save(self.image3.path)
		if self.image4:
				
			image4 = Image.open(self.image4)
			i_width, i_height = image4.size
			max_size = (1000,750)
			try:
			    for orientation in ExifTags.TAGS.keys():
			        if ExifTags.TAGS[orientation]=='Orientation':
			            break
			    exif=dict(image4._getexif().items())

			    if exif[orientation] == 3:
			        image4=image4.rotate(180, expand=True)
			    elif exif[orientation] == 6:
			        image4=image4.rotate(270, expand=True)
			    elif exif[orientation] == 8:
			        image4=image4.rotate(90, expand=True)
			    image4.save(self.image4.path)

			except (AttributeError, KeyError, IndexError):
			    # cases: image don't have getexif
			    pass
			image4.thumbnail(max_size, Image.ANTIALIAS)
			image4.save(self.image4.path)

# def upload_location(instance, filename):
# 	return "%s/%s" %(instance.id, filename)
class UserProfile(models.Model):
	user =  models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
	image = models.ImageField(
            null=True,
            blank=True)
	slug = AutoSlugField(populate_from='user',null=True, blank=True, unique=True)
	shelf = models.ManyToManyField(Book, blank=True)
#to activate shell, do {{ object.shelf.all }} in templates.

	
	def __unicode__(self):
		return self.user.username
# this is required when you override save functions

class Rating(models.Model):
	user =  models.ForeignKey(UserProfile, related_name='userprofile', blank=True,null=True)
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
