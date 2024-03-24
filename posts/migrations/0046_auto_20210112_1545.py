# Generated by Django 3.1.4 on 2021-01-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0045_category_disc'),
    ]

    operations = [
        migrations.AddField(
            model_name='blankpage',
            name='disc',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Add In Disclaimer'),
        ),
        migrations.AddField(
            model_name='blog',
            name='disc',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Add In Disclaimer'),
        ),
        migrations.AddField(
            model_name='maincourse',
            name='disc',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Add In Disclaimer'),
        ),
        migrations.AddField(
            model_name='post',
            name='disc',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Add In Disclaimer'),
        ),
        migrations.AddField(
            model_name='subcat',
            name='disc',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Add In Disclaimer'),
        ),
        migrations.AlterField(
            model_name='category',
            name='disc',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Add In Disclaimer'),
        ),
    ]