# Generated by Django 2.2.11 on 2020-03-24 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeePattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_pattern_class_name', models.CharField(default=' ', max_length=50)),
                ('fee_pattern_type', models.CharField(default='', max_length=50)),
                ('fee_pattern_tution_fee', models.IntegerField(default='0')),
                ('fee_pattern_academic_fee', models.IntegerField(default='0')),
            ],
        ),
    ]
