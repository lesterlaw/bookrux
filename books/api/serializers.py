from rest_framework.serializers import ModelSerializer

from books.models import Book

class BookListSerializer(ModelSerializer):
	class Meta:
		model = Book
		fields = [
			'title',
			'genre',
			'description',
			'price',
			'slug',
		]
class BookDetailSerializer(ModelSerializer):
	class Meta:
		model = Book
		fields = [
			'author',
			'title',
			'genre',
			'description',
			'personal_review',
			'price',
			'published_date',
		]