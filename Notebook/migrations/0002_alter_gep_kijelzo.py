# Generated by Django 5.0.2 on 2024-03-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gep',
            name='kijelzo',
            field=models.FloatField(),
        ),
    ]