# Generated by Django 3.1.7 on 2021-04-10 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photatoes', '0005_auto_20210409_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='portfolioPhotographer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photatoes.photographer'),
        ),
    ]
