# Generated by Django 3.1.4 on 2020-12-31 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_auto_20201230_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='totalDays',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='log',
            name='totalDays',
            field=models.TextField(blank=True, null=True),
        ),
    ]