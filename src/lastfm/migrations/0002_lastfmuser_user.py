# Generated by Django 3.0.3 on 2020-03-31 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('telegram', '0001_initial'),
        ('lastfm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lastfmuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lastfm_user', to='telegram.TelegramUser', verbose_name='User'),
        ),
    ]
