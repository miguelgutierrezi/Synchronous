# Generated by Django 2.1 on 2018-10-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickBackend', '0005_subject_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='endTime',
            field=models.CharField(default='00:00', max_length=5),
        ),
        migrations.AddField(
            model_name='subject',
            name='starTime',
            field=models.CharField(default='00:00', max_length=5),
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]