# Generated by Django 4.0.4 on 2022-06-21 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0014_healthcentre_user_policeauthority_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policeauthority',
            name='neighborhood_id',
        ),
        migrations.RemoveField(
            model_name='policeauthority',
            name='user',
        ),
        migrations.DeleteModel(
            name='HealthCentre',
        ),
        migrations.DeleteModel(
            name='PoliceAuthority',
        ),
    ]