# Generated by Django 3.0.6 on 2020-06-12 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_bloodpressurepatient_bloodpressurepractitioner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloodpressurepractitioner',
            old_name='filter_bp',
            new_name='filter_bp_x',
        ),
        migrations.AddField(
            model_name='bloodpressurepractitioner',
            name='filter_bp_y',
            field=models.IntegerField(default=0),
        ),
    ]
