# Generated by Django 3.1.1 on 2020-09-12 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_update_app', '0003_auto_20200912_0725'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classmodel',
            old_name='data',
            new_name='date',
        ),
    ]
