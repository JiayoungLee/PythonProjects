# Generated by Django 2.1.7 on 2020-09-07 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gzbd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_email',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]