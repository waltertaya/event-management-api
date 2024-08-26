# Generated by Django 5.1 on 2024-08-26 14:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'events',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('response', models.BooleanField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
