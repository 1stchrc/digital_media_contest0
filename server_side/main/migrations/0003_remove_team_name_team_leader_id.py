# Generated by Django 4.1.7 on 2023-10-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_team_category_remove_team_tags_team_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='name',
        ),
        migrations.AddField(
            model_name='team',
            name='leader_id',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
