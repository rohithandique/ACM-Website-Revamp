# Generated by Django 2.2.7 on 2020-03-23 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acm', '0003_auto_20191210_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='poster_link',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='report_link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
