# Generated by Django 5.2.4 on 2025-07-31 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
