# Generated by Django 5.1.4 on 2025-01-06 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pocket', '0002_customuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
