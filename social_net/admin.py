from django.contrib import admin
from .models import User

# Register your models here.

admin.site.register(User)  # Make it visible on the admin page
