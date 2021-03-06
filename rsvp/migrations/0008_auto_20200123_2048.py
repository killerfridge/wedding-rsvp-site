# Generated by Django 2.2.7 on 2020-01-23 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0007_auto_20200123_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='attending',
            field=models.BooleanField(choices=[(True, 'Will Be Attending'), (False, 'Will Not Be Attending')], default=False, verbose_name='Presence'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='dietary',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Dietary Requirements'),
        ),
    ]
