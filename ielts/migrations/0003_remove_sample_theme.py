# Generated by Django 5.1.4 on 2024-12-21 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ielts', '0002_remove_firstpart_audio_remove_secondpart_audio_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='theme',
        ),
    ]
