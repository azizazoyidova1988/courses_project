# Generated by Django 3.2.5 on 2021-07-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='image/'),
        ),
    ]
