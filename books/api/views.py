from rest_framework.generics import (
	ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
	)

from books.models import Book

from .serializers import BookListSerializer, BookDetailSerializer

class BookListAPIView(ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookListSerializer

class BookDetailAPIView(RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookDetailSerializer
	lookup_field = 'slug'
	# lookup_url_kwarg = 'slug'

class BookDeleteAPIView(DestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookDetailSerializer
	lookup_field = 'slug'
	# lookup_url_kwarg = 'slug'

class BookUpdateAPIView(UpdateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookDetailSerializer
	lookup_field = 'slug'
	# lookup_url_kwarg = 'slug'