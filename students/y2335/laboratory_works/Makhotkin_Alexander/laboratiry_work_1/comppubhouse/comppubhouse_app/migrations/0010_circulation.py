# Generated by Django 3.0.7 on 2020-06-30 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comppubhouse_app', '0009_auto_20200629_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Circulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('count', models.DecimalField(decimal_places=0, max_digits=5)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comppubhouse_app.Book')),
            ],
        ),
    ]
