from django import forms
from .models import Note


class AddNoteForm(forms.ModelForm):
	class Meta:
		model = Note
		fields = ['name', 'subject', 'description', 'price', 'condition', 'image1', 'image2', 'image3', 'image4']