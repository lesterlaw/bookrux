from django.contrib import admin
from .models import Book, UserProfile, Rating
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'genre', 'sold')
	list_filter = ['published_date', 'genre', 'sold']
	search_fields = ['title', 'description']
admin.site.register(Book, BookAdmin)

# our new model to add at the bottom

class UserProfileInline(admin.TabularInline):
    model = UserProfile
    can_delete = False

class RatingInline(admin.TabularInline):
	model = Rating
	fk_name = 'user'
	extra = -3

class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, RatingInline,) 


admin.site.unregister(User)
admin.site.register(User, UserAdmin)