# Generated by Django 3.2.5 on 2021-07-05 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20210704_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='commenter',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.course'),
        ),
    ]
