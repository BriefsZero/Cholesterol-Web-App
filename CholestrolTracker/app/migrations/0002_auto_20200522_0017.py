# Generated by Django 3.0.6 on 2020-05-22 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cholesterolpractitioner',
            name='original_practitioner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='original_practitioner', to='app.Practitioner'),
        ),
    ]
