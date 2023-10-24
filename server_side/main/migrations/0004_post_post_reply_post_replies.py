# Generated by Django 4.1.7 on 2023-10-24 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_team_name_team_leader_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Nice post.')),
                ('content', models.TextField(default='Some content...')),
                ('author_id', models.CharField(max_length=64)),
                ('tags', models.JSONField(default=list)),
                ('private_flag', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='post_reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='Nice reply.')),
                ('author', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='replies',
            field=models.ManyToManyField(to='main.post_reply'),
        ),
    ]
