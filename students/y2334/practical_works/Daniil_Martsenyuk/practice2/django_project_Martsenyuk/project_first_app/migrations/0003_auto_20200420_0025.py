# Generated by Django 3.0.5 on 2020-04-19 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0002_auto_20200416_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
