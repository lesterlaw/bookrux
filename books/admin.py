from django.contrib import admin
from .models import Book, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Book)

# our new model to add at the bottom

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)