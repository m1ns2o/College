# Generated by Django 2.2.6 on 2019-12-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collegeInfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college_info',
            name='location',
            field=models.CharField(max_length=200),
        ),
    ]
