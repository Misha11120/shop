# Generated by Django 5.1.2 on 2024-11-24 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_shoe_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
