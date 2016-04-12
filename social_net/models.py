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

    def register(self):
        self.verified = True
        p = Profile(user = self, registration_datetime = timezone.now())
        p.save(force_insert=True)

    def __str__(self):
        return self.name + " " + self.last_name


# Profile model contains additional information of a user (one-to-one)

class Profile(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    registration_datetime = models.DateTimeField()
    picture = models.ImageField(upload_to='profile_pic/', blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    additional_info = models.TextField(blank=True)
    topic = models.ManyToManyField('Topic', blank=True)

    class Meta:
        db_table = "profile"

    def __str__(self):
        return self.user.name + " " + self.user.last_name + " " + self.registration_date.strftime("%c")


# Message model contains all the messages of particular profile (many-to-one)

class Message(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    sender_profile = models.OneToOneField('Profile')
    datetime = models.DateTimeField()
    text = models.CharField(max_length=255) # 255 chars is max message limit
    read = models.BooleanField(default=False)

    class Meta:
        db_table = "message"

    def __str__(self):
        return self.read + " " + self.text + " " + self.datetime.strftime("%c")


# Student list model connects student profile with teachers profiles (many-to-one)

class StudentList(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    teacher_profile = models.ForeignKey('Profile')

    class Meta:
        db_table = "student_list"

    def __str__(self):
        return self.profile + " " + self.teacher_profile


# Subscription model connects profile with subscriptions (many-to-one)

class Subscription(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    teacher_profile = models.ForeignKey('Profile')
    topic = models.ForeignKey('Topic')

    class Meta:
        db_table = "subscription"

    def __str__(self):
        return self.profile + " " + self.teacher_profile + " " + self.topic


# Topic model contains topics with their description

class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "topic"

    def __str__(self):
        return self.name


# Comment model contains comments to the educational content (many-to-one)

class Comment(models.Model):
    edu_content = models.ForeignKey('EducationalContent', on_delete=models.CASCADE)
    parent = models.ForeignKey('Comment', blank=True, null=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    text = models.CharField(max_length=255) # 255 chars is max comment limit
    read = models.BooleanField(default=False)

    class Meta:
        db_table = "comment"

    def __str__(self):
        return self.read + " " + self.text + " " + self.datetime.strftime("%c")


# Notification types model

class NotificationType(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "notification_type"

    def __str__(self):
        return self.name


# Notifications model contains notifications of different types temporary

class Notification(models.Model):
    type = models.ForeignKey('NotificationType', on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    comment = models.ForeignKey('Comment', blank=True, null=True)
    teacher_profile = models.ForeignKey('Profile', blank=True, null=True)
    topic = models.ForeignKey('Topic',  blank=True, null=True)

    class Meta:
        db_table = "notification"

    def __str__(self):
        return self.type + " " + self.datetime.strftime("%c")


# Educational content model contains all educational information for publishing

class EducationalContent(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    topic = models.ForeignKey('Topic')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024)
    text = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    url = models.URLField()
    data = models.BinaryField()

    class Meta:
        db_table = "educational_content"

    def __str__(self):
        return self.topic + " " + self.name + " " + self.published
