from django.db import models
from django.utils import timezone


# User model contains basic registration information

class User(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    verified = models.BooleanField(default=False)

    class Meta:
        db_table = "user"

    def verify(self):
        self.verified = True
        pass # TBD

    def __str__(self):
        return self.name + " " + self.last_name


# Profile model contains additional information of a user

class Profile(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    registration_date = models.DateTimeField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True) # TBD
    description = models.CharField(max_length=255, blank=True, null=True)
    additional_info = models.TextField(blank=True)

    class Meta:
        db_table = "profile"

    def register(self): # wrong place
        self.registration_date = timezone.now()
        self.save()

    def __str__(self):
        return self.user.name + " " + self.user.last_name + " " + self.registration_date.strftime("%c")