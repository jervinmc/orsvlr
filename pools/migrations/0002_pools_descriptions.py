# Generated by Django 4.0 on 2022-01-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pools',
            name='descriptions',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='descriptions'),
        ),
    ]