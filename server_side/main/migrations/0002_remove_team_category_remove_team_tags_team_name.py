# Generated by Django 4.1.7 on 2023-10-22 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='category',
        ),
        migrations.RemoveField(
            model_name='team',
            name='tags',
        ),
        migrations.AddField(
            model_name='team',
            name='name',
            field=models.TextField(default='法兰不死队'),
        ),
    ]
