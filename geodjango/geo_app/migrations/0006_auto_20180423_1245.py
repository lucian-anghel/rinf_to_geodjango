# Generated by Django 2.0.4 on 2018-04-23 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_app', '0005_auto_20180422_1804'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operationalpoint',
            old_name='opp_geom',
            new_name='geom',
        ),
    ]