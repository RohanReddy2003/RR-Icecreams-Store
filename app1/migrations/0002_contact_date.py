# Generated by Django 4.2.4 on 2023-08-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
