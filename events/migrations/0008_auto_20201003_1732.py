# Generated by Django 3.0.5 on 2020-10-03 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20201003_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='athletes',
        ),
        migrations.AddField(
            model_name='event',
            name='athletes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Athlete'),
        ),
    ]
