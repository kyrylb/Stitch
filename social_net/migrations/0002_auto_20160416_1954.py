# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-16 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_net', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_profiles', to='social_net.Profile'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender_profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender_profile', to='social_net.Profile'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_list_profiles', to='social_net.Profile'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='teacher_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_list_teacher_profiles', to='social_net.Profile'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_profiles', to='social_net.Profile'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='teacher_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscription_teacher_profiles', to='social_net.Profile'),
        ),
    ]
