from django.contrib import admin
from .models import Message, Chat
# Register your models here.
class ChatInline(admin.TabularInline):
	model = Message

class ChatAdmin(admin.ModelAdmin):
	inlines = (ChatInline,)

admin.site.register(Chat, ChatAdmin)
