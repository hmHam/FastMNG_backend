# Generated by Django 3.0.3 on 2020-03-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatery', '0002_auto_20200304_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.IntegerField(choices=[(0, '空き'), (1, '予約'), (2, '使用中')], default=0),
        ),
    ]