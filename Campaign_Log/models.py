from django.db import models

# Create your models here.

class CampaignManager(models.Manager):
    pass

class Campaign(models.Model):
    objects = CampaignManager()
    title = models.CharField(max_length = 100, blank=True, default='')

class LogManager(models.Manager):
    pass

class Log(models.Model):
    objects = LogManager()
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    campaign = models.ForeignKey('Campaign', related_name='logs')

    class Meta:
        ordering = ('created',)

class CharacterManager(models.Manager):
    pass

class Character(models.Model):
    objects = CharacterManager()
    name = models.CharField(max_length = 100, blank=True, default='')
    description = models.TextField()
    assosiatedLocation = models.ForeignKey('Location', blank=True, null=True)
    campaign = models.ForeignKey('Campaign', related_name='characters')

class LocationManager(models.Manager):
    pass

class Location(models.Model):
    objects = LocationManager()
    name = models.CharField(max_length = 100)
    description = models.TextField(blank=True)
    locationType = models.CharField(default='None',max_length=100)
    campaign = models.ForeignKey('Campaign', related_name='locations')
    pass
