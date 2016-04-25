from __future__ import unicode_literals

from django.db import models
from PIL import Image, ExifTags
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from likert_field.models import LikertField

# Create your models here.
class Review(models.Model):
	author = models.ForeignKey(User)
	writer = models.CharField(max_length=100)
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
	rating = LikertField(blank=False)
	image1 = models.ImageField(
            null=True,
            blank=True)
	def save(self, *args, **kwargs):
		# this is required when you override save functions
		super(Review, self).save(*args, **kwargs)
	# our new code

		if self.image1:
				
			image1 = Image.open(self.image1)
			i_width, i_height = image1.size
			max_size = (750,750)
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

	def __unicode__(self):
		return self.title

	def publish(self):
		published_date = timezone.now()
		published_date.save()
