# Generated by Django 3.0.5 on 2020-06-24 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almanac_calendar', '0003_auto_20200623_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
