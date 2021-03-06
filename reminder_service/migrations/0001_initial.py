# Generated by Django 4.0.4 on 2022-04-17 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('priority', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('due_date', models.DateTimeField(blank=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='reminder_service.editor')),
            ],
        ),
        migrations.CreateModel(
            name='ShareReminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor', models.ManyToManyField(to='reminder_service.editor')),
                ('reminder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reminder_service.reminder')),
            ],
        ),
    ]
