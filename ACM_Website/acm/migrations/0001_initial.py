# Generated by Django 2.2.6 on 2019-12-04 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SIG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Special_people',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('post', models.CharField(max_length=25)),
                ('fb_link', models.CharField(max_length=500)),
                ('linkedin_link', models.CharField(max_length=500)),
                ('image_path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('report_link', models.CharField(max_length=500)),
                ('poster_link', models.CharField(max_length=500)),
                ('sig_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acm.SIG')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=5000)),
                ('sig_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acm.SIG')),
            ],
        ),
    ]
