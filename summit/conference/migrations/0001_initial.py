# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('contact', models.EmailField(null=True, max_length=254, blank=True)),
                ('link', models.URLField(null=True, blank=True)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SponsorshipOption',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=60)),
                ('on_site', models.BooleanField(default=True)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('status', models.CharField(max_length=15, choices=[('PROP', 'proposed'), ('ACC', 'accepted'), ('CAN', 'cancelled')])),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('slides_link', models.URLField(null=True, blank=True)),
                ('video_link', models.URLField(null=True, blank=True)),
                ('featured', models.BooleanField(default=None)),
                ('presenter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sponsor',
            name='options',
            field=models.ManyToManyField(to='conference.SponsorshipOption'),
        ),
    ]
