# Generated by Django 2.1 on 2018-10-14 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('value', models.FloatField(default=1)),
                ('grade', models.FloatField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('credits', models.IntegerField(default=1)),
                ('grade', models.FloatField(default=1)),
                ('teacher', models.CharField(default=' ', max_length=100)),
                ('starTime', models.CharField(default='00:00', max_length=5)),
                ('endTime', models.CharField(default='00:00', max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='activity',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickBackend.Subject'),
        ),
    ]
