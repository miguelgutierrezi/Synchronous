# Generated by Django 2.1 on 2018-10-14 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickBackend', '0002_auto_20181014_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='quickBackend.Subject'),
        ),
    ]
