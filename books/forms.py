from django import forms
from .models import Book, UserProfile, Rating
from django.core.validators import MaxValueValidator
from django.core.mail import send_mail
from ckeditor.widgets import CKEditorWidget
from django.conf import settings
from widgets import AdvancedFileInput
class AddBookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title','tags', 'author', 'description', 'personal_review', 'condition', 'genre', 'price', 'image1', 'image2', 'image3', 'image4']
		labels = {
			'title': ('What is the name of the book?'),
			'author': ('Who wrote this book?'),
			'description':('Details and Condition?'),
			'personal_review': ('Your thoughts/summary?'),
			'price': ('How much are you selling for?'),

		}

class UserProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['image',]

class AddRatingForm(forms.ModelForm):
	class Meta:
		model = Rating
		fields = ['rate', 'feedback',]

class MassMailForm(forms.Form):
	subject = forms.CharField(required=True)
	content = forms.CharField(
		required=True,
		widget=CKEditorWidget()
	)
	def __init__(self, *args, **kwargs):
		super(MassMailForm, self).__init__(*args, **kwargs)
		self.fields['subject'].label = "What the fuck do you want the title to be?!"
		self.fields['content'].label = "What the fuck do you want to tell all the fucking users in bookrux?!"

class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	)
	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "Your name:"
		self.fields['contact_email'].label = "Your email:"
		self.fields['content'].label = "What do you want to say?"