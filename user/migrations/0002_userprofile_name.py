# Generated by Django 3.0.8 on 2020-12-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
