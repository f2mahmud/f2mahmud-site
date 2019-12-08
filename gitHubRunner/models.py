from django.db import models
from django.urls import reverse
import uuid


# Create your models here.

class Platform(models.Model):
    name = models.CharField(null=False, max_length=15)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Category(models.Model):
    name = models.CharField(null=False, max_length=15)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class DataSource(models.Model):
    name = models.URLField(null=False)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Project(models.Model):
    title = models.CharField('Title', max_length=50, null=False)
    description = models.TextField('Description')
    link = models.URLField('Link')
    gitHubLink = models.URLField('Git')
    platform = models.ManyToManyField(Platform)
    category = models.ManyToManyField(Category)
    dataSource = models.ManyToManyField(DataSource)

    STATUS = (
        ('c', 'Concept'),
        ('p', 'Planning'),
        ('d', 'Development'),
        ('f', 'Finished'),
        ('u', 'Updating')
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='c',
        help_text='Status of the idea',
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this project."""
        return reverse('project-detail', args=[str(self.id)])
