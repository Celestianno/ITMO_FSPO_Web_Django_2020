# Generated by Django 3.1 on 2020-10-31 01:57

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_purchase_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=300)),
                ('coat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.coat')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
