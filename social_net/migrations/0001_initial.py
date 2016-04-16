# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-16 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('text', models.CharField(max_length=255)),
                ('read', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='EducationalContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1024)),
                ('text', models.TextField(blank=True)),
                ('published', models.BooleanField(default=False)),
                ('url', models.URLField()),
                ('data', models.BinaryField()),
            ],
            options={
                'db_table': 'educational_content',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('text', models.CharField(max_length=255)),
                ('read', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social_net.Comment')),
            ],
            options={
                'db_table': 'notification',
            },
        ),
        migrations.CreateModel(
            name='NotificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'notification_type',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_datetime', models.DateTimeField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pic/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_info', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_list_profile', to='social_net.Profile')),
                ('teacher_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_net.Profile')),
            ],
            options={
                'db_table': 'student_list',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_profile', to='social_net.Profile')),
                ('teacher_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_net.Profile')),
            ],
            options={
                'db_table': 'subscription',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'topic',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='subscription',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_net.Topic'),
        ),
        migrations.AddField(
            model_name='profile',
            name='topic',
            field=models.ManyToManyField(blank=True, to='social_net.Topic'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='social_net.User'),
        ),
        migrations.AddField(
            model_name='notification',
            name='teacher_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social_net.Profile'),
        ),
        migrations.AddField(
            model_name='notification',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social_net.Topic'),
        ),
        migrations.AddField(
            model_name='notification',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_net.NotificationType'),
        ),
        migrations.AddField(
            model_name='message',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_profile', to='social_net.Profile'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='social_net.Profile'),
        ),
        migrations.AddField(
            model_name='educationalcontent',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_net.Profile'),
        ),
        migrations.AddField(
            model_name='educationalcontent',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_net.Topic'),
        ),
        migrations.AddField(
            model_name='comment',
            name='edu_content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_net.EducationalContent'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social_net.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_net.Profile'),
        ),
    ]
