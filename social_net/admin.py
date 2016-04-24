from django.contrib import admin
from .models import User, Profile, Topic, Subscription

# Register your models here.

myModels = [User, Profile, Topic, Subscription, ]  # Iterable list

admin.site.register(myModels)  # Make it visible on the admin page
