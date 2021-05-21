# Generated by Django 3.0.5 on 2020-09-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200917_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='event_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]