# Generated by Django 3.0.8 on 2020-12-19 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20201219_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='certificate',
            field=models.BooleanField(default=False),
        ),
    ]