# Generated by Django 3.0.8 on 2020-12-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_cart_certificate'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/certificate'),
        ),
    ]
