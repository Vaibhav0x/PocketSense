# Generated by Django 5.1.4 on 2025-01-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pocket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
