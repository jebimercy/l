# Generated by Django 4.1.7 on 2023-03-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_cry_mercy', '0002_student_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(default='Nairobi', max_length=50),
        ),
    ]
