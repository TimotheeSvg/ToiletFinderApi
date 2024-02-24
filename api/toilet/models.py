from django.db import models


class Toilet(models.Model):
    toiletId = models.IntegerField(primary_key=True, unique=True)
    toiletLatitude = models.FloatField(null=False, blank=False)
    toiletLongitude = models.FloatField(null=False, blank=False)
    toiletName = models.CharField(max_length=255, null=False, blank=False)
    toiletStreet = models.CharField(max_length=255, null=False, blank=False)
    toiletCity = models.CharField(max_length=255, null=False, blank=False)
    toiletCountry = models.CharField(max_length=255, null=False, blank=False)
    toiletDirection = models.CharField(max_length=512, null=False, blank=False)

    class Meta:
        db_table = 'toilet'
        app_label = 'toilet'

        constraints = [
            models.UniqueConstraint(
                fields=['toiletLatitude', 'toiletLongitude'],
                name='unique_coo'
            )
        ]
