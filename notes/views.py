from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, HttpResponse
from django.views import generic
from .models import Note
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from .forms import AddNoteForm
from django.utils import timezone
# Create your views here.
class NoteList(generic.ListView):
	model = Note
	template_name = 'notes/notelist.html'
	context_object_name = 'notes'
	paginate_by = 12

	# def get_queryset(self):
	# 	query = self.request.GET.get('q')
	# 	filtered = self.request.GET.get('fil')
	# 	if query and not filtered:
	# 		return Note.objects.filter(
	# 			Q(title__icontains=query)
	# 			).order_by('sold', '-published_date')
	# 	elif filtered and not query:
	# 		return Note.objects.filter(
	# 			Q(genre__icontains=filtered)).order_by('sold', '-published_date')
	# 	elif filtered and query:
	# 		return Note.objects.filter(
	# 			Q(title__icontains=query) &
	# 			Q(genre__icontains=filtered)).order_by('sold', '-published_date')
	# 	return Note.objects.order_by('sold', '-published_date')

class NoteDetail(generic.DetailView):
	model = Note
	template_name = 'notes/notedetail.html'

@csrf_protect
@login_required
def AddNote(request):
	if request.method == "POST":
		form = AddNoteForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('notes:notedetail', slug=post.slug)
	else:
		form = AddNoteForm()
	return render(request, 'notes/noteedit.html', {'form': form})
@csrf_protect
@login_required
def EditNote(request, slug):
	post = get_object_or_404(Note, slug=slug)
	if request.user == post.user:
		if request.method == "POST":
			form = AddNoteForm(request.POST, instance=post, files=request.FILES)
			if form.is_valid():
				post = form.save(commit=False)
				post.user = request.user
				post.published_date = timezone.now()
				post.save()
				return redirect('notes:notedetail', slug=slug)
		else:
			form = AddNoteForm(instance=post)
		return render(request, 'notes/noteedit.html', {'form': form, 'object': post})
	else:
		messages.warning(request,"You are not allowed to edit this!")
		return redirect(reverse('notes:notelist'))
@login_required
def DeleteNote(request, slug):
	post = get_object_or_404(Note, slug=slug)
	if request.user == post.user:
		post.delete()
		return redirect('notes:notelist')
	else:
		messages.warning(request, 'You are not allowed to delete this post!')
		return redirect(reverse('notes:notelist'))
