from django.contrib import admin

# Register your models here.
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user_name', 'full_name')
