# Generated by Django 4.0 on 2022-01-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='customer_name')),
                ('contact_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='contact_number')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='email')),
                ('service_type', models.CharField(blank=True, max_length=255, null=True, verbose_name='contact_number')),
                ('date_start', models.DateField(blank=True, null=True, verbose_name='date_start')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='date_end')),
                ('descriptions', models.CharField(blank=True, max_length=255, null=True, verbose_name='descriptions')),
                ('price', models.CharField(blank=True, max_length=255, null=True, verbose_name='price')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='status')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]