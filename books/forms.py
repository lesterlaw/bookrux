from django import forms
from .models import Book, UserProfile

class AddBookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'description', 'personal_review', 'genre', 'price']

class UserProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['image',]