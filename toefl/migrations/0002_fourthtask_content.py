# Generated by Django 5.1.4 on 2024-12-21 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toefl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fourthtask',
            name='content',
            field=models.CharField(blank=True, max_length=5120, null=True),
        ),
    ]
