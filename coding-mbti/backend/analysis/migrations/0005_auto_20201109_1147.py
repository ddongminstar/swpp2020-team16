# Generated by Django 3.1.2 on 2020-11-09 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0004_auto_20201109_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solutionreport',
            old_name='predcition',
            new_name='prediction',
        ),
    ]