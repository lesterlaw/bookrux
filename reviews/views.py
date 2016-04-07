from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, HttpResponse
from django.views import generic
from models import Review
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .forms import AddReviewForm
from django.utils import timezone
# Create your views here.

class ReviewList(generic.ListView):
	model = Review
	template_name = 'reviews/reviewlist.html'
	context_object_name = 'reviews'
	# def get_queryset(self):
	# 	query = self.request.GET.get('q')
	# 	filtered = self.request.GET.get('fil')
	# 	if query and not filtered:
	# 		return Review.objects.filter(
	# 			Q(title__icontains=query)
	# 			).order_by('sold', '-published_date')
	# 	elif filtered and not query:
	# 		return Review.objects.filter(
	# 			Q(genre__icontains=filtered)).order_by('sold', '-published_date')
	# 	elif filtered and query:
	# 		return Review.objects.filter(
	# 			Q(title__icontains=query) &
	# 			Q(genre__icontains=filtered)).order_by('sold', '-published_date')
	# 	return Review.objects.order_by('sold', '-published_date')


class ReviewDetail(generic.DetailView):
	model = Review
	template_name = 'reviews/reviewdetail.html'

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
	if request.user == post.user:
		if request.method == "POST":
			form = AddReviewForm(request.POST, instance=post, files=request.FILES)
			if form.is_valid():
				post = form.save(commit=False)
				post.user = request.user
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
	if request.user == post.user:
		post.delete()
		return redirect('reviews:reviewlist')
	else:
		messages.warning(request, 'You are not allowed to delete this post!')
		return redirect(reverse('reviews:reviewlist'))
