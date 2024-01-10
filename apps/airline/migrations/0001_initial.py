# Generated by Django 4.2.9 on 2024-01-08 07:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=5, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='airline_logos/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]