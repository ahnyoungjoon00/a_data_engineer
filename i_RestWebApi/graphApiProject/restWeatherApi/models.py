from django.db import models

# Create your models here.
class WeatherSeoul(models.Model):
    date = models.DateTimeField(primary_key=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    month = models.CharField(max_length=10, blank=True, null=True)
    day = models.CharField(max_length=10, blank=True, null=True)
    avg_tmp = models.FloatField(blank=True, null=True)
    high_tmp = models.FloatField(blank=True, null=True)
    low_tmp = models.FloatField(blank=True, null=True)
    cloud_cover = models.FloatField(blank=True, null=True)
    day_rain = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_seoul'