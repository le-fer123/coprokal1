# Generated by Django 5.1.4 on 2024-12-20 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('audio', models.FileField(upload_to='ielts/firstpart')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SecondPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('audio', models.FileField(upload_to='ielts/secondpart')),
                ('content', models.TextField()),
                ('followup', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ThirdPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('audio', models.FileField(upload_to='ielts/thirdpart')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=128)),
                ('first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ielts.firstpart')),
                ('second', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ielts.secondpart')),
                ('third', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ielts.thirdpart')),
            ],
        ),
    ]
