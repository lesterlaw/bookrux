from __future__ import unicode_literals

from django.db import models
from PIL import Image, ExifTags
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image, ExifTags
from django.utils.crypto import get_random_string
from likert_field.models import LikertField

class Note(models.Model):
	Subject = (
		('Primary', (
			('prienglish','English'),
			('primath','Math'),
			('primothertongue','Mother Tongue'),
			('priscience','Science'),
			)
		),
		('Secondary', (
			('secenglish','English'),
			('secmath','Math'),
			('secmothertongue','Mother Tongue'),
			('secscience','Science'),
			('sechumanities','Humanities'),
			)
		),
		('Junior College', (
			('jcgp','General Paper'),
			('jcmath','Math'),
			('jcmothertongue','Mother Tongue'),
			('jcscience','Science'),
			('jchumanities','Humanities'),
			)
		),
		('Polytechnic', (
			('polybusiness','Business'),
			('polydesign','Design'),
			('polyengineering','Engineering'),
			('polyit','IT'),
			('polymedia','Media'),
			('polyscience','Science'),
			)
		),
		('ITE', (
			('itebusiness','Business'),
			('itedesign','Design'),
			('iteengineering','Engineering'),
			('iteit','IT'),
			('itemedia','Media'),
			('itescience','Science'),
			)
		),
		('University', (
			('unibusiness','Business'),
			('unidesign','Design'),
			('uniengineering','Engineering'),
			('uniit','IT'),
			('unimedia','Media'),
			('uniscience','Science'),
			)
		),
	)
	user = models.ForeignKey(User)
	name = models.CharField(max_length=100)
	subject = models.CharField(max_length=100, choices=Subject)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	published_date = models.DateTimeField(default=timezone.now)
	likes = models.IntegerField(default=0)
	condition = LikertField(blank=False)
	slug = models.SlugField(
		unique=True,
		default=get_random_string,
		max_length=13,
	)
	book = models.BooleanField(default=False)
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
			return self.name

	def save(self, *args, **kwargs):
		# this is required when you override save functions
		super(Note, self).save(*args, **kwargs)
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
		if self.image2:
				
			image2 = Image.open(self.image2)
			i_width, i_height = image2.size
			max_size = (750,750)
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
			max_size = (750,750)
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
			max_size = (750,750)
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
