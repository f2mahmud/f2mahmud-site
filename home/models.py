from django.db import models


# Create your models here.

class Education(models.Model):
    name = models.CharField(null=False, max_length=35)
    institution = models.CharField(max_length=30)
    yearStarted = models.IntegerField()
    yearEnded = models.IntegerField()
    description = models.TextField(max_length=4000)


class WorkExperience(models.Model):
    position = models.CharField(null=False, max_length=30)
    companyName = models.TextField(max_length=40)
    logo = models.ImageField(upload_to="gallery", null=True)
    startDate = models.DateField()
    endDate = models.DateField(null=True)
    description = models.TextField(max_length=4000)
