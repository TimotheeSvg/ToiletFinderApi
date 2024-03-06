# Generated by Django 4.2.7 on 2024-03-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Toilet',
            fields=[
                ('toiletId', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('toiletLatitude', models.FloatField()),
                ('toiletLongitude', models.FloatField()),
                ('toiletName', models.CharField(max_length=255)),
                ('toiletStreet', models.CharField(max_length=255)),
                ('toiletCity', models.CharField(max_length=255)),
                ('toiletCountry', models.CharField(max_length=255)),
                ('toiletDirection', models.CharField(max_length=512)),
                ('toiletUpVote', models.IntegerField(default=0)),
                ('toiletDownVote', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'toilet',
            },
        ),
        migrations.AddConstraint(
            model_name='toilet',
            constraint=models.UniqueConstraint(fields=('toiletLatitude', 'toiletLongitude'), name='unique_coo'),
        ),
    ]
