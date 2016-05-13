from django import forms
from .models import Chat, Message

class SendMessageForm(forms.ModelForm):
	class Meta:
		model = Message
		fields = ['message',]
        widgets = {
            'text': forms.TextInput(
                attrs={'id': 'post-text', 'required': True, 'placeholder': 'Say something...'}
            ),
        }