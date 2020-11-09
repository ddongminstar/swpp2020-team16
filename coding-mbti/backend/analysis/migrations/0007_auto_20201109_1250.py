# Generated by Django 3.1.2 on 2020-11-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0006_auto_20201109_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solutionreport',
            old_name='probability',
            new_name='erase_probability',
        ),
        migrations.RemoveField(
            model_name='solutionreport',
            name='prediction',
        ),
        migrations.AddField(
            model_name='solutionreport',
            name='erase_prediction',
            field=models.IntegerField(choices=[(1, 'Um'), (2, 'Ti')], null=True),
        ),
        migrations.AddField(
            model_name='solutionreport',
            name='ml_prediction',
            field=models.IntegerField(choices=[(1, 'Um'), (2, 'Ti')], null=True),
        ),
        migrations.AddField(
            model_name='solutionreport',
            name='ml_probability',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='solutionreport',
            name='style_prediction',
            field=models.IntegerField(choices=[(1, 'Um'), (2, 'Ti')], null=True),
        ),
        migrations.AddField(
            model_name='solutionreport',
            name='style_probability',
            field=models.FloatField(default=0),
        ),
    ]