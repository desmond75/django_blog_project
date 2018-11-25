# Generated by Django 2.0.6 on 2018-06-06 11:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(choices=[('news', 'News'), ('artist', 'Artist'), ('lyrics', 'Lyrics'), ('showbiz', 'Showbiz'), ('album', 'Albums'), ('leaks', 'Leaks'), (None, 'Tags')], db_column='Tags', db_index=True, max_length=20),
        ),
        migrations.AddField(
            model_name='comments',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Article'),
        ),
    ]
