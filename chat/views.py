from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, HttpResponse
from .models import Message, Chat
from django.db.models import Q
from django.utils import timezone
from django.http import JsonResponse
from django.db import IntegrityError
from books.models import Book
from django.contrib import messages
from .forms import SendMessageForm
# Create your views here.
def Redirect(request):
	return redirect("chats:inbox")

def Inbox(request):
	chats = Chat.objects.all().filter(
		Q(recipient__exact=request.user) |
		Q(sender__exact=request.user))

	return render(request, 'chats/inbox.html', { "chats" : chats })

def ChatDetail(request, slug):
	chat = get_object_or_404(Chat, slug=slug)
	return render(request, 'chats/chatdetail.html', {"chat": chat})

def CreateChat(request,slug):
	product = get_object_or_404(Book, slug=slug)
	try:
		chat = Chat(book=product, sender=request.user, recipient=product.user)
		chat.save()
		return redirect("chats:chatdetail", slug=chat.slug)
	except IntegrityError:
		messages.warning(request, 'Chat already exists')
		return redirect("books:bookdetail", slug=product.slug)

def SendMessage(request, slug):
	chat = get_object_or_404(Chat, slug=slug)
	if request.method == "POST":
		form = SendMessageForm(request.POST or None)
		if form.is_valid():
			post = form.save(commit=False)
			msg = post.message
			post.chat = chat
			post.sender = request.user
			post.recipient = chat.recipient
			post.send_at = timezone.now()
			post.save()
			return redirect("chats:chatdetail", slug=chat.slug)
	else:
		form = SendMessageForm()
	return render(request, 'chats/sendmessage.html', {'form': form})