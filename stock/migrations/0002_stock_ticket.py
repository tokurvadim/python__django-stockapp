# Generated by Django 4.2.6 on 2023-10-11 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='ticket',
            field=models.CharField(default='NULL', max_length=4),
        ),
    ]
