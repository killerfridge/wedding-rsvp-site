# Generated by Django 2.2.7 on 2020-01-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0009_auto_20200123_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.CharField(max_length=200)),
                ('day_question', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='guest',
            name='attending',
            field=models.BooleanField(choices=[(True, 'Will Be Attending'), (False, 'Will Not Be Attending')], default=True, verbose_name='Presence'),
        ),
    ]
