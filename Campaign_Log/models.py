from django.db import models

# Create your models here.
LOCATION_TYPES = (('F', 'Forrest'), ('C','City'), ('V','Village'), ('P','Planes'), ('OC','Ocean'), ('OT','Other'))

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
    assosiatedLocation = models.ForeignKey('Location')
    campaign = models.ForeignKey('Campaign', related_name='characters')

class LocationManager(models.Manager):
    pass

class Location(models.Model):
    objects = LocationManager()
    name = models.CharField(max_length = 100, blank=True, default='')
    description = models.TextField()
    locationType = models.CharField(choices = LOCATION_TYPES, max_length=100)
    campaign = models.ForeignKey('Campaign', related_name='locations')
    pass
