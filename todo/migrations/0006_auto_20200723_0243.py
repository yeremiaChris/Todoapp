# Generated by Django 3.0.8 on 2020-07-23 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20200723_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
