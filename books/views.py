from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, HttpResponse
from django.template.loader import render_to_string, get_template
from django.template import Context
from django.core.urlresolvers import reverse
from django.db.models import Q
from .models import Book, UserProfile, Rating
from django.contrib.auth.models import User
from django.views import generic
from .forms import AddBookForm, UserProfileUpdateForm, AddRatingForm, ContactForm
from django.utils import timezone
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import stripe
stripe.api_key = settings.STRIPE_SECRET

from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from serializers import BookSerializer, UserSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def homepage(request):
	books = Book.objects.all().order_by('-published_date').filter(sold=False)[:6]
	return render(request, 'books/homepage.html', {'books':books})
	
class BookList(generic.ListView):
	model = Book
	template_name = 'books/booklist.html'
	context_object_name = 'books'
	paginate_by = 12

	def get_queryset(self):
		query = self.request.GET.get('q')
		filtered = self.request.GET.get('fil')
		if query and not filtered:
			return Book.objects.filter(
				Q(title__contains=query)
				).order_by('sold', '-published_date')
		elif filtered and not query:
			return Book.objects.filter(
				Q(genre__contains=filtered)).order_by('sold', '-published_date')
		elif filtered and query:
			return Book.objects.filter(
				Q(title__contains=query) &
				Q(genre__contains=filtered)).order_by('sold', '-published_date')
		return Book.objects.order_by('sold', '-published_date')



class BookDetail(generic.DetailView):
	model = Book
	template_name = 'books/bookdetail.html'

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(BookDetail, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['key'] = settings.STRIPE_PUBLISHABLE
		return context

@login_required
def charge(request, slug):
	book = get_object_or_404(Book, slug=slug)
	if book.sold == False:

		# grab the logged in user, and the object the user "owns"
		if request.method != "POST":
			return redirect(reverse("books:booklist"))
		if not 'stripeToken' in request.POST:
			messages.error(request, "Something went wrong")
		else:
			customer = stripe.Customer.create(email=request.POST['stripeEmail'],
				source=request.POST['stripeToken'],)
			amount = (int(book.price) + 2)* 100
			charge = stripe.Charge.create(
				customer=customer.id,
				amount=amount,
				currency='sgd',
				description="OneTimeCharge",)
			book.sold = True
			book.save()

			user = request.user
			subject = 'Payment confirmation'

			from_email = settings.EMAIL_HOST_USER
			email = request.POST['stripeEmail']
			recipient_list = [email, settings.EMAIL_HOST_USER]
			html_message = render_to_string('books/payment_email.html', {'book':book, 'user':user})

			email = EmailMessage('Payment Confirmation', html_message, from_email,
			recipient_list)
			email.content_subtype = 'html'
			email.send()
			messages.success(request, 'You have successfully made payment!')
			return redirect(reverse('books:booklist'))
	else:

		messages.success(request, 'You cannot buy this anymore!')
		return redirect('books:bookdetail', slug=book.slug)

@csrf_protect
@login_required
def AddBook(request):
	if request.method == "POST":
		form = AddBookForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('books:bookdetail', slug=post.slug)
	else:
		form = AddBookForm()
	return render(request, 'books/bookedit.html', {'form': form})
@csrf_protect
@login_required
def EditBook(request, slug):
	post = get_object_or_404(Book, slug=slug)
	if request.user == post.user:
		if request.method == "POST":
			form = AddBookForm(request.POST, instance=post, files=request.FILES)
			if form.is_valid():
				post = form.save(commit=False)
				post.user = request.user
				post.published_date = timezone.now()
				post.save()
				return redirect('books:bookdetail', slug=slug)
		else:
			form = AddBookForm(instance=post)
		return render(request, 'books/bookedit.html', {'form': form, 'object': post})
	else:
		messages.warning(request,"You are not allowed to edit this!")
		return redirect(reverse('books:booklist'))
@login_required
def DeleteBook(request, slug):
	post = get_object_or_404(Book, slug=slug)
	if request.user == post.user:
		post.delete()
		return redirect('books:booklist')
	else:
		messages.warning(request, 'You are not allowed to delete this post!')
		return redirect(reverse('books:booklist'))

def sold(request, slug):
	post = get_object_or_404(Book, slug=slug)
	if post.sold == False:
		if request.user == post.user:
			post.sold = True
			post.save()
			messages.success(request, 'This book has been successfully marked as sold')
			return redirect('books:bookdetail', slug=post.slug)
		else:
			messages.warning(request, 'You are not allowed to mark this book as sold')
			return redirect('books:bookdetail', slug=post.slug)
	else:
		messages.warning(request, 'This book has already been marked as sold')
		return redirect('books:bookdetail', slug=post.slug)

def rentcomingsoon(request):
	return render(request, 'books/rentcomingsoon.html')

@login_required
def AddRating(request, slug):
	userx = get_object_or_404(UserProfile, slug=slug)
	if not userx == request.user:
		if request.method == "POST":
			form = AddRatingForm(request.POST or None)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.user = userx
				post.save()
				messages.success(request, 'You have successfully added a feedback for this user!')
				return redirect('user_profile_detail', slug=userx.slug)
		else:
			form = AddRatingForm()
		return render(request, 'books/addrating.html', {'form':form, 'userx':userx})
	else:
		messages.warning(request, "You cannot leave feedback for yourself")
		return redirect('books:booklist')

# class GenreDetail(generic.ListView):
# 	model = Book
# 	template_name = 'books/genredetail.html'

# 	def get_queryset(self):
# 		genre = Book.
def GenreDetail(request, genre):
	books = Book.objects.all()
	clean = books.filter(genre__icontains=genre).order_by('sold')
	paginator = Paginator(clean, 12)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
	return render(request, 'books/genredetail.html', {'books':clean, 'contacts': contacts})


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

def ContactView(request):
	form_class = ContactForm

	# new logic!
	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = request.POST.get('contact_name', '')
			contact_email = request.POST.get('contact_email', '')
			form_content = request.POST.get('content', '')

			# Email the profile with the 
			# contact information
			template = get_template('books/contact_template.txt')
			context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
			})
			content = template.render(context)

			email = EmailMessage("New contact form submission", content,"Bookrux" +'', ['bookrux@gmail.com'],headers = {'Reply-To': contact_email })
			email.send()
			messages.success(request, 'Thank you for your feedback!')
			return redirect('contactview')

	return render(request, 'books/contact.html', {
		'form': form_class,
	})

# def UserProfileDetail(request, slug):
# 	object = get_object_or_404(UserProfile, slug=slug)
# 	books = Book.objects.all().order_by('sold','-published_date').filter(user__userprofile__slug__iexact=slug)
# 	ratings = Rating.objects.all().filter(user__slug__iexact=slug)
# 	paginator = Paginator(books, 12) # Show 25 contacts per page

# 	page = request.GET.get('page')
# 	try:
# 		contacts = paginator.page(page)
# 	except PageNotAnInteger:
# 		# If page is not an integer, deliver first page.
# 		contacts = paginator.page(1)
# 	except EmptyPage:
# 		# If page is out of range (e.g. 9999), deliver last page of results.
# 		contacts = paginator.page(paginator.num_pages)


# 	return render(request, 'books/userprofile_detail.html', {'object':object,'books':books,'ratings':ratings})

class UserProfileDetail(generic.DetailView):
	model = UserProfile
	template_name = "books/userprofile_detail.html"

	def get_context_data(self, **kwargs):
		context = super(UserProfileDetail, self).get_context_data(**kwargs)
		context['books'] = Book.objects.all().order_by('sold','-published_date').filter(user__userprofile__slug__iexact=self.kwargs['slug'])
		context['ratings'] = Rating.objects.all().filter(user__slug__iexact=self.kwargs['slug'])

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
	login_required = True
	fields = ('image',)
	def user_passes_test(self, request):
		if request.user.is_authenticated():
			self.object = self.get_object()
			return self.object.user == request.user
		return False

	def dispatch(self, request, *args, **kwargs):
		if not self.user_passes_test(request):
			messages.warning(request,"You are not allowed to edit this!")
			return redirect('homepage')
		return super(UserProfileUpdate, self).dispatch(
            request, *args, **kwargs)

	# def get(self, request, *args, **kwargs):
	# 	assure_user_profile_exists(kwargs['pk'])
	# 	return (super(UserProfileUpdate, self).
	# 			get(self, request, *args, **kwargs))

# def BookListUser(request, pk):
# 	user = User.objects.get(pk=pk)
# 	books = Book.objects.all().order_by('-published_date')
# 	return render(request, 'books/profilelist.html', {'books':books, 'user':user})

def LikeBook(request):
	if request.user.is_authenticated():
		slug = request.GET.get('slug', None)
		post = get_object_or_404(Book, slug=slug)
		shelf = request.user.userprofile.shelf
		if not post in request.user.userprofile.shelf.all():
			shelf.add(post)
			post.likes += 1
			post.save()
		else:
			shelf.remove(post)
			post.likes -= 1
			post.save()
		return redirect('books:booklist')
	else:
		messages.error(request, "Log in or sign up to like an image!")
		return redirect('auth_login')

class BookViewSet(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer