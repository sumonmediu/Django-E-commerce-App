# Generated by Django 3.0.8 on 2020-12-30 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=10),
        ),
    ]
