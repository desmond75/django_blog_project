# Generated by Django 2.0.6 on 2018-06-05 03:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='Title', db_index=True, max_length=80)),
                ('body', models.TextField(db_column='Body', db_index=True)),
                ('image', models.ImageField(db_column='Image', upload_to='images')),
                ('tags', models.CharField(choices=[('news', 'News'), ('artist', 'Artist'), ('lyrics', 'Lyrics'), ('showbiz', 'Showbiz'), ('albulm', 'Albums'), ('leaks', 'Leaks')], db_column='Tags', db_index=True, max_length=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
