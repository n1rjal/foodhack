# Generated by Django 3.0.5 on 2020-06-05 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_auto_20200605_1316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='leftover',
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
