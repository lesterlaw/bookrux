from rest_framework import serializers, viewsets
from .models import Book, UserProfile

from django.contrib.auth.models import User


class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Book
		fields = ('title', 'description', 'price', 'user', 'genre',)
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'is_superuser')
# ViewSets define the view behavior.