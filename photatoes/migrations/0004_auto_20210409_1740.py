# Generated by Django 3.1.7 on 2021-04-09 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photatoes', '0003_auto_20210409_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageName', models.CharField(max_length=150)),
                ('imageAperture', models.IntegerField()),
                ('imageShutterSpeed', models.IntegerField()),
                ('imageISO', models.IntegerField()),
                ('imageCamera', models.CharField(max_length=150)),
                ('imageFile', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographerName', models.CharField(max_length=100)),
                ('photographerProfileDesc', models.TextField()),
                ('photographerTwitter', models.URLField()),
                ('photographerLinkedIn', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='PhotographerPortfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photographerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photatoes.portfolio')),
                ('portfolioID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photatoes.photographer')),
            ],
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolioImageOne',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo1', to='photatoes.image'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolioImageThree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo3', to='photatoes.image'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='portfolioImageTwo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photo2', to='photatoes.image'),
        ),
    ]
