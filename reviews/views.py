from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, HttpResponse
from django.views import generic
from models import Review
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .forms import AddReviewForm
from django.utils import timezone
from django.db.models import Q, F
from books.models import Book
from notes.models import Note
# Create your views here.

class ReviewList(generic.ListView):
	model = Review
	template_name = 'reviews/reviewlist.html'
	context_object_name = 'reviews'
	def get_queryset(self):
		query = self.request.GET.get('q')
		filtered = self.request.GET.get('fil')
		if query and not filtered:
			return Review.objects.filter(
				Q(title__icontains=query)
				).order_by('-published_date')
		elif filtered and not query:
			return Review.objects.filter(
				Q(genre__icontains=filtered)).order_by('-published_date')
		elif filtered and query:
			return Review.objects.filter(
				Q(title__icontains=query) &
				Q(genre__icontains=filtered)).order_by('-published_date')
		return Review.objects.order_by('-published_date')


# class ReviewDetail(generic.DetailView):
# 	model = Review
# 	template_name = 'reviews/reviewdetail.html'
# 	def get_context_data(self, **kwargs):
# 		context = super(ReviewDetail, self).get_context_data(**kwargs)
# 		print queryset
# 		context['similarbooks'] = Book.objects.all().order_by('sold','-published_date').filter(
# 			title__icontains=queryset)
# 		print context['similarbooks']
# 		return context

def ReviewDetail(request, slug):
	review = get_object_or_404(Review, slug=slug)
	similarbooks = Book.objects.all().filter(Q(title__icontains=review.title) &
		Q(sold=False))
	print similarbooks
	return render(request, 'reviews/reviewdetail.html', {'object':review, 'similarbooks': similarbooks})
@csrf_protect
@login_required
def AddReview(request):
	if request.method == "POST":
		form = AddReviewForm(request.POST or None)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('reviews:reviewdetail', slug=post.slug)
	else:
		form = AddReviewForm()
	return render(request, 'reviews/reviewedit.html', {'form': form})
@csrf_protect
@login_required
def EditReview(request, slug):
	post = get_object_or_404(Review, slug=slug)
	if request.user == post.author or request.user.is_staff:
		if request.method == "POST":
			form = AddReviewForm(request.POST, instance=post, files=request.FILES)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.published_date = timezone.now()
				post.save()
				return redirect('reviews:reviewdetail', slug=slug)
		else:
			form = AddReviewForm(instance=post)
		return render(request, 'reviews/reviewedit.html', {'form': form, 'object': post})
	else:
		messages.warning(request,"You are not allowed to edit this!")
		return redirect(reverse('reviews:reviewlist'))
@login_required
def DeleteReview(request, slug):
	post = get_object_or_404(Review, slug=slug)
	if request.user == post.author or request.user.is_staff:
		post.delete()
		return redirect('reviews:reviewlist')
	else:
		messages.warning(request, 'You are not allowed to delete this post!')
		return redirect(reverse('reviews:reviewlist'))


def sold(request, slug):
	post = get_object_or_404(Review, slug=slug)
	if post.sold == False:
		if request.user == post.author or request.user.is_staff:
			post.sold = True
			post.save()
			messages.success(request, 'This review has been successfully marked as sold')
			return redirect('reviews:reviewdetail', slug=post.slug)
		else:
			messages.warning(request, 'You are not allowed to mark this book as sold')
			return redirect('reviews:reviewdetail', slug=post.slug)
	else:
		messages.warning(request, 'This book has already been marked as sold')
		return redirect('reviews:reviewdetail', slug=post.slug)
