# Generated by Django 3.1.1 on 2020-09-14 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_update_app', '0005_auto_20200912_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classmodel',
            name='classname',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='classmodel',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='classmodel',
            name='url',
            field=models.TextField(null=True),
        ),
    ]
