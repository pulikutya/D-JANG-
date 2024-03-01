# Generated by Django 5.0.2 on 2024-03-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gyarto', models.CharField(max_length=255)),
                ('tipus', models.CharField(max_length=255)),
                ('kijelzo', models.IntegerField()),
                ('memoria', models.IntegerField()),
                ('merevlemez', models.IntegerField()),
                ('videovezerlo', models.CharField(max_length=255)),
                ('processzorid', models.IntegerField()),
                ('oprendszerid', models.IntegerField()),
                ('db', models.IntegerField()),
            ],
            options={
                'verbose_name': 'gep',
                'verbose_name_plural': 'gepek',
            },
        ),
        migrations.CreateModel(
            name='oprendszer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'oprendszer',
                'verbose_name_plural': 'oprendszer',
            },
        ),
        migrations.CreateModel(
            name='processzor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gyarto', models.CharField(max_length=255)),
                ('tipus', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'processzor',
                'verbose_name_plural': 'processzorok',
            },
        ),
    ]
