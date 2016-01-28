from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.db.models import Q
from .models import Book, UserProfile, assure_user_profile_exists
from django.contrib.auth.models import User
from django.views import generic
from .forms import AddBookForm, UserProfileUpdateForm
from django.utils import timezone

from rest_framework import viewsets
from serializers import BookSerializer, UserSerializer

class BookList(generic.ListView):
	model = Book
	template_name = 'books/booklist.html'
	context_object_name = 'books'
	paginate_by = 12

	def get_queryset(self):
		query = self.request.GET.get('q')
		if query:
			return Book.objects.filter(
				Q(title__icontains=query) |
				Q(description__icontains=query)).order_by('-published_date')
		return Book.objects.order_by('-published_date')

class BookDetail(generic.DetailView):
	model = Book
	template_name = 'books/bookdetail.html'

def AddBook(request):
	if request.method == "POST":
		form = AddBookForm(request.POST or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('books:bookdetail', slug=post.slug)
	else:
		form = AddBookForm()
	return render(request, 'books/bookedit.html', {'form': form})

def EditBook(request, slug):
	post = get_object_or_404(Book, slug=slug)
	if request.method == "POST":
		form = AddBookForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('books:bookdetail', slug=slug)
	else:
		form = AddBookForm(instance=post)
	return render(request, 'books/bookedit.html', {'form': form})

def DeleteBook(request, slug):
	post = get_object_or_404(Book, slug=slug).delete()
	return redirect('books:booklist')

class GenreList(generic.ListView):
	model = Book
	template_name = "books/genrelist.html"

#WORKING FUNCTION BASED VIEW STARTS HERE
# def UserProfileDetail(request, pk):
# 	profile = UserProfile.objects.get(pk=pk)
# 	user = User.objects.get(pk=pk)
# 	books = Book.objects.all().order_by('-published_date')
# 	return render(request, 'books/userprofile_detail.html', {'object': profile, 'books':books, 'user':user})
#ENDS HERE

class UserProfileDetail(generic.DetailView):
	model = UserProfile
	template_name = "books/userprofile_detail.html"

	# def get_queryset(self, **kwargs):
	# 	username = User.get_username()

	def get_context_data(self, **kwargs):
		context = super(UserProfileDetail, self).get_context_data(**kwargs)
		context['books'] = Book.objects.all().order_by('-published_date')
		context['shelf'] = UserProfile.objects.all()
		return context

# def UserProfileUpdate(request, username):
# 	profile = User.objects.get(username=username)
# 	if request.method == 'post':
# 		form = UserProfileUpdateForm(request.post, instance=profile)
# 		if form.is_valid():
# 			profile = form.save(commit=False)
# 			profile.save()

# 			#INSERT SUCCESS MESSAGE HERE EVENTUALLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 			return redirect('books:booklist')
# 	else:
# 		form = UserProfileUpdateForm(instance=profile) 
# 	return render(request, 'books/userprofile_form.html', {'object':profile, 'UserProfile':UserProfile})



class UserProfileUpdate(generic.UpdateView):
	model = UserProfile
	template_name = "books/userprofile_form.html"
	fields = ('image',)

	# def get(self, request, *args, **kwargs):
	# 	assure_user_profile_exists(kwargs['pk'])
	# 	return (super(UserProfileUpdate, self).
	# 			get(self, request, *args, **kwargs))

# def BookListUser(request, pk):
# 	user = User.objects.get(pk=pk)
# 	books = Book.objects.all().order_by('-published_date')
# 	return render(request, 'books/profilelist.html', {'books':books, 'user':user})


class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer