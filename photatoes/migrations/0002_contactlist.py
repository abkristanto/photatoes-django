# Generated by Django 3.1.7 on 2021-04-09 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photatoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
        ),
    ]
