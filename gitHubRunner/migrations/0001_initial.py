# Generated by Django 2.2.1 on 2019-11-24 03:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('description', models.CharField(max_length=2000, verbose_name='Description')),
                ('link', models.URLField(verbose_name='Link')),
                ('gitHubLink', models.URLField(verbose_name='Git')),
                ('status', models.CharField(blank=True, choices=[('c', 'Concept'), ('p', 'Planning'), ('d', 'Development'), ('f', 'Finished'), ('u', 'Updating')], default='c', help_text='Book availability', max_length=1)),
                ('category', models.ManyToManyField(to='gitHubRunner.Category')),
                ('dataSource', models.ManyToManyField(to='gitHubRunner.DataSource')),
                ('platform', models.ManyToManyField(to='gitHubRunner.Platform')),
            ],
        ),
    ]
