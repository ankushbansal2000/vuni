# Generated by Django 3.0.5 on 2020-04-11 17:13

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20200327_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_image', models.ImageField(upload_to=register.models.upload_path)),
            ],
        ),
        migrations.AlterField(
            model_name='student_details',
            name='student_academic_year',
            field=models.CharField(default='NotGiven ', max_length=50),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='student_admission_category',
            field=models.CharField(default=' NotGiven', max_length=50),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='student_batch',
            field=models.CharField(default='NotGiven ', max_length=50),
        ),
        migrations.AlterField(
            model_name='student_details',
            name='student_fee_category',
            field=models.CharField(default=' NotGiven', max_length=50),
        ),
    ]
