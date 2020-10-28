# Generated by Django 3.1.1 on 2020-10-24 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20201024_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='account',
            field=models.ManyToManyField(blank=True, to='bank.Account'),
        ),
        migrations.AlterField(
            model_name='client',
            name='contract_code',
            field=models.ManyToManyField(blank=True, to='bank.Contract'),
        ),
    ]
