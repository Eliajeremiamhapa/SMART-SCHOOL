from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Kama User tayari yupo Registered, tunamtoa kwanza kisha tunamrudisha
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

@admin.register(User)
class MyUserAdmin(UserAdmin):
    # Hapa unaweza kuongeza urembo zaidi ukitaka kuona nani ni Mwanafunzi au Mwalimu
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')