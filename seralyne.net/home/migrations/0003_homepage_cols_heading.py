# Generated by Django 5.0.8 on 2024-08-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='cols_heading',
            field=models.CharField(blank=True, help_text='Write a heading for the columns', max_length=255),
        ),
    ]
