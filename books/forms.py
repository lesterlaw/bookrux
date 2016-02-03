from django import forms
from .models import Book, UserProfile, Rating

class AddBookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'description', 'personal_review', 'genre', 'price']
		labels = {
            'title': ('What is the name of the book?'),
            'description':('Details and Condition?'),
            'personal_review': ('Your thoughts/summary?'),
            'price': ('How much are you selling?'),
        }

class UserProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['image',]

class AddRatingForm(forms.ModelForm):
	class Meta:
		model = Rating
		fields = ['rate', 'feedback',]