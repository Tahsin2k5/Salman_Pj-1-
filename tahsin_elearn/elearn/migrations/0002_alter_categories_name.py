# Generated by Django 4.1.7 on 2023-09-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
