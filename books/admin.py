from django.contrib import admin
from .models import Book, UserProfile, Rating
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Book)

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