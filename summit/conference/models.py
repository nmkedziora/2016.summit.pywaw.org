from django.conf import settings
from django.db import models

# TODO: do we need a Conference model and all those models should be related to the specific Conference?


class Talk(models.Model):

    class Status:
        proposed = 'PROP'
        accepted = 'ACC'
        cancelled = 'CAN'

    STATUSES = (
        (Status.proposed, 'proposed'),
        (Status.accepted, 'accepted'),
        (Status.cancelled, 'cancelled'),
    )

    status = models.CharField(max_length=15, choices=STATUSES)
    presenter = models.ForeignKey(settings.AUTH_USER_MODEL)

    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateTimeField(blank=True, null=True)  # only accepted talks appearing in agenda need to have it
    slides_link = models.URLField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=None)


class SponsorshipOption(models.Model):
    name = models.CharField(max_length=60)
    on_site = models.BooleanField(default=True)  # for special kinds of sponsorhip - after party, etc.
    order = models.IntegerField()  # order of appearance on site


class Sponsor(models.Model):
    options = models.ManyToManyField(SponsorshipOption)

    contact = models.EmailField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField()
    description = models.TextField(blank=True)
