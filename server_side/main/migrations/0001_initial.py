# Generated by Django 4.1.7 on 2023-10-19 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.CharField(default='', max_length=64, primary_key=True, serialize=False)),
                ('tags', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user_data')),
            ],
        ),
    ]
