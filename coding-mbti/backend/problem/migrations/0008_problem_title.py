# Generated by Django 3.1.2 on 2020-11-11 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0007_auto_20201111_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='title',
            field=models.CharField(default='', max_length=31),
        ),
    ]