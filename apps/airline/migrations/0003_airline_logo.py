# Generated by Django 4.2.9 on 2024-01-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0002_remove_airline_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='airline',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='airline_logos/'),
        ),
    ]
