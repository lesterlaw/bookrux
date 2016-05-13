from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone
from books.models import Book
from notes.models import Note
from django.utils.crypto import get_random_string

# Create your models here.(null=True, blank=True)

class Chat(models.Model):
	book = models.ForeignKey(Book, blank=True, null=True)
	note = models.ForeignKey(Note, blank=True, null=True)
	sender = models.ForeignKey(User, related_name="sender")
	recipient = models.ForeignKey(User, related_name="recipient")
	slug = models.SlugField(
		unique=True,
		default=get_random_string,
		max_length=13,
	)
	def __unicode__(self):
		if self.book:
			return self.book.title
		elif self.note:
			return self.note.name
	class Meta:
		unique_together = ('book', 'sender', 'recipient')

class Message(models.Model):
	chat = models.ForeignKey(Chat)
	sender = models.ForeignKey(User, related_name="msender")
	recipient = models.ForeignKey(User, related_name="mrecipient")
	message = models.TextField()
	sent_at = models.DateTimeField(default=timezone.now)
	read_at = models.DateTimeField

	def __unicode__(self):
		return self.message