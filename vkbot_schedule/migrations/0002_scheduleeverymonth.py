# Generated by Django 2.0.1 on 2018-01-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vkbot_schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleEveryMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
                ('days', models.CharField(max_length=60)),
            ],
        ),
    ]
